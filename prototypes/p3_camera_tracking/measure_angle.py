"""P3 camera tracking test: measure shoulder angle from short phone clips.

Name each clip <view>_<angle>_<rep>.mp4, for example side_090_1.mp4 or
45deg_120_3.mp4, where <angle> is the reference angle marked on the wall chart.
Film one clip per hold, about 3 seconds long, with the whole upper body in frame.

Usage:
    python measure_angle.py path/to/clips --out results.csv
"""
import argparse
import csv
import math
import re
import statistics
from collections import defaultdict
from pathlib import Path

CLIP_NAME = re.compile(r"^(?P<view>[A-Za-z0-9]+)_(?P<angle>\d{1,3})_(?P<rep>\d+)$")
VIDEO_TYPES = {".mp4", ".mov", ".avi", ".m4v"}
MIN_VISIBILITY = 0.5

# MediaPipe Pose landmark indexes: (shoulder, elbow, hip).
LEFT_ARM = (11, 13, 23)
RIGHT_ARM = (12, 14, 24)


def parse_clip_name(path):
    match = CLIP_NAME.match(Path(path).stem)
    if not match:
        return None
    return match["view"], int(match["angle"]), int(match["rep"])


def shoulder_angle(shoulder, elbow, hip):
    """Angle at the shoulder between the upper arm and the trunk, in degrees."""
    arm = (elbow[0] - shoulder[0], elbow[1] - shoulder[1])
    trunk = (hip[0] - shoulder[0], hip[1] - shoulder[1])
    arm_length = math.hypot(*arm)
    trunk_length = math.hypot(*trunk)
    if arm_length == 0 or trunk_length == 0:
        return None
    cosine = (arm[0] * trunk[0] + arm[1] * trunk[1]) / (arm_length * trunk_length)
    return math.degrees(math.acos(max(-1.0, min(1.0, cosine))))


def angle_from_landmarks(landmarks, width, height):
    """Use whichever arm the model can see better. Returns None if neither is clear."""
    arms = [
        (min(landmarks[i].visibility for i in arm), arm)
        for arm in (LEFT_ARM, RIGHT_ARM)
    ]
    visibility, arm = max(arms, key=lambda item: item[0])
    if visibility < MIN_VISIBILITY:
        return None
    # Pixels, not normalised coordinates, so a non-square frame does not skew the angle.
    points = [(landmarks[i].x * width, landmarks[i].y * height) for i in arm]
    return shoulder_angle(*points)


def measure_clip(path, pose):
    """Median angle over the clip, so brief wobble in a hold does not affect it."""
    import cv2

    capture = cv2.VideoCapture(str(path))
    angles = []
    while True:
        ok, frame = capture.read()
        if not ok:
            break
        height, width = frame.shape[:2]
        result = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if result.pose_landmarks:
            angle = angle_from_landmarks(result.pose_landmarks.landmark, width, height)
            if angle is not None:
                angles.append(angle)
    capture.release()
    return (statistics.median(angles) if angles else None), len(angles)


def summarise(rows):
    """Mean absolute error for each camera view and reference angle."""
    groups = defaultdict(list)
    for row in rows:
        if row["measured"] is None:
            continue
        error = abs(row["measured"] - row["reference"])
        groups[(row["view"], row["reference"])].append(error)
        groups[(row["view"], "all")].append(error)
    return {key: statistics.mean(errors) for key, errors in groups.items()}


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("clips", type=Path)
    parser.add_argument("--out", type=Path, default=Path("results.csv"))
    args = parser.parse_args()

    import mediapipe as mp

    rows = []
    with mp.solutions.pose.Pose(static_image_mode=False, model_complexity=1) as pose:
        for path in sorted(args.clips.iterdir()):
            if path.suffix.lower() not in VIDEO_TYPES:
                continue
            parsed = parse_clip_name(path)
            if parsed is None:
                print(f"Skipped {path.name}: name is not <view>_<angle>_<rep>")
                continue
            view, reference, rep = parsed
            measured, frames = measure_clip(path, pose)
            rows.append({"clip": path.name, "view": view, "reference": reference,
                         "rep": rep, "measured": measured, "frames_used": frames})
            shown = "no pose found" if measured is None else f"{measured:.1f} deg"
            print(f"{path.name}: {shown} ({frames} frames)")

    with args.out.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["clip", "view", "reference", "rep",
                                                  "measured", "frames_used", "error"])
        writer.writeheader()
        for row in rows:
            error = None if row["measured"] is None else row["measured"] - row["reference"]
            writer.writerow({**row, "error": error})

    print("\nMean absolute error (degrees)")
    for (view, reference), error in sorted(summarise(rows).items(), key=str):
        print(f"  {view:>8}  {str(reference):>4}  {error:5.1f}")
    print(f"\nSaved {args.out}")


if __name__ == "__main__":
    main()
