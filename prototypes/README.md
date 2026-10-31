# Interim prototypes

## P1: progress tracker

Open the [web link](https://claude.ai/artifact/6eKZh5YK9Trb4vgazCfDg2), or open `p1_progress_tracker/index.html` in a browser. All data are fictional, and the expected range is illustrative.

The screens have neutral names so they do not give away the answer. Show them in a different random order to each participant.

| Screen | Patient at week 14 | Correct answer |
|---|---|---|
| 1 | 98°, feels good | Behind (expected 110–135°) |
| 2 | 125°, feels good | On track |
| 3 | 146°, feels good | Ahead |

Screen 1 is the key test: does the participant notice the patient is behind even though they feel good?

## P2: exercise session flow

Open the [web link](https://claude.ai/artifact/MCof3qxjA9kXrffwU7wZJs), or open `p2_session_flow/index.html` in a browser, ideally on a phone or in a narrow window. The web link uses the test photo, because live camera preview is not available there. Participants tap through one session: choose an exercise, read the instructions, set up the phone, follow along, report pain and see the result. The exercises are placeholders, and the repetitions count automatically, so participants do not need to do any movement.

The set-up screen shows a live camera preview where the browser allows it. Otherwise it offers a test photo taken with the phone camera. The picture stays on the device and is not saved or uploaded.

At the end, open "For the facilitator" to read the set-up time and the time spent on each screen. Reload the page between participants. To open one screen directly, add its number to the address, for example `index.html#3`.

## P3: camera tracking test

### Set-up

Use a short folder path such as `C:\p3`, because the install can fail on long Windows paths. MediaPipe is pinned to 0.10.14 because the script uses its older `solutions` interface.

```
python -m venv C:\p3\env
C:\p3\env\Scripts\pip install mediapipe==0.10.14
```

### Filming

1. Draw reference lines at 30°, 60°, 90°, 120° and 150° on a wall chart, using a protractor, centred at shoulder height.
2. Stand with your side to the camera, and raise your arm to each line. Hold for about 3 seconds.
3. Film one clip per hold, three times per angle, then repeat with the camera at about 45°.
4. Name the clips `<view>_<angle>_<rep>.mp4`, for example `side_090_1.mp4` or `45deg_120_3.mp4`, and put them in one folder.

Keep the whole upper body in frame, and wear a top that contrasts with the background.

### Running it

```
C:\p3\env\Scripts\python measure_angle.py C:\p3\clips --out results.csv
```

The script prints the mean absolute error for each camera view and angle, and saves each clip's measurement to `results.csv`.
