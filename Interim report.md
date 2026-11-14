# Rehabilitation Adherence After Rotator Cuff Repair

## CDE4301 Innovation & Design Capstone — Interim Report

**Project team:** Team Scapullama (Raghavi and Phyllis)  
**Semester:** Semester 1, AY2026/27  
**Supervisor(s):** Mark Chong Seow Khoon

## Table of Contents

1. [Objective, Scope and Context](#1-objective-scope-and-context)
2. [Methodology / Concept Development](#2-methodology--concept-development)
3. [Fabrication of Prototypes](#3-fabrication-of-prototypes)
4. [Testing](#4-testing)
5. [Analysis](#5-analysis)
6. [Discussion of Problems and Project Plan](#6-discussion-of-problems-and-project-plan)
7. [Conclusion](#7-conclusion)
8. [Individual Contributions](#8-individual-contributions)
9. [References](#references)
10. [Appendices](#appendices)
   - [Appendix A: Review of existing solutions](#appendix-a-review-of-existing-solutions)
   - [Appendix B: Summary of stakeholder interviews](#appendix-b-summary-of-stakeholder-interviews)
   - [Appendix C: Patient survey](#appendix-c-patient-survey)
   - [Appendix D: Concept Generation & Screening](#appendix-d-concept-generation--screening)
   - [Appendix E: Test session findings](#appendix-e-test-session-findings)
   - [Appendix F: Semester 2 prototypes](#appendix-f-semester-2-prototypes)

## 1. Objective, Scope and Context

### 1.1 Objective and scope

Recovery after rotator cuff repair (RCR) relies on months of home-based rehabilitation, yet patients receive little guidance or feedback between physiotherapy appointments. This project aims to design a home rehabilitation support system, ReMotion, that helps patients adhere to their prescribed programme after RCR, so that they progress safely towards clinically meaningful functional recovery by six months. 

- **In scope:** adults in Singapore in the home-based phase of rehabilitation after RCR, particularly working patients; fitting exercises into daily routines; feedback on exercise technique; tracking shoulder range of motion and strength against the expected recovery trajectory; guidance on acceptable pain and when to progress; and between-visit progress summaries for physiotherapists.
- **Out of scope:** replacing physiotherapists or changing surgical or rehabilitation protocols; diagnosing complications; non-surgical management of rotator cuff tears; and clinical effectiveness trials.

By the end of Semester 2, we aim to deliver a functional prototype evaluated with patients and physiotherapists against the specifications in Section 1.4. This is feasible because we have regular access to our clinical mentor, physiotherapists who have offered to help recruit participants, and industry fellows on our team with product development experience.

### 1.2 Context

Rotator cuff tears are among the most common causes of shoulder pain and disability (Simon et al., 2023), and their prevalence rises with age (Sripathi & Agrawal, 2024). When conservative management fails or the tear is large, patients may undergo surgical rotator cuff repair (RCR) (Sambandam, 2015).

Recovery then follows a phased protocol lasting several months, from sling immobilisation and passive exercises to active movement and strengthening (Sambandam, 2015). Most of this is done unsupervised at home, and adherence is low (Burns et al., 2021). Physiotherapists we interviewed estimated that 30–50% of patients do not do their home exercises and up to 20–30% drop out of public-sector physiotherapy. This can lead to repeat care and residual stiffness, which clinicians said can extend recovery from about 6 to 10 months ([Appendix B, B.5](#b5-estimates-of-adherence-and-drop-off) and Theme 7). In Singapore's public hospitals, follow-ups are often 3–4 weeks apart, so adherence depends on patients' own discipline to perform the exercises at home.

Our interviews with 6 patients, 10 physiotherapists and 3 surgeons ([Appendix B](#appendix-b-summary-of-stakeholder-interviews)) and a survey of 6 patients ([Appendix C](#appendix-c-patient-survey)) identified four barriers to adherence:

1. **Lack of time and discipline**, especially after patients return to work (7/10 physiotherapists; 3/6 survey respondents).
2. **Uncertainty about technique:** patients forget exercises or cannot tell whether their form is correct (8/10 physiotherapists).
3. **Misjudging progress:** patients often stop once they feel "good enough", around three months after surgery, before strength and range are restored (7/10 physiotherapists).
4. **Pain and fear of movement:** patients interpret pain as damage to the repair and stop exercising, leading to stiffness (7/10 physiotherapists; 2/6 survey respondents).

Of the 17 existing solutions we reviewed ([Appendix A](#appendix-a-review-of-existing-solutions)), digital exercise platforms offer videos and reminders but no technique feedback, while sensor- and camera-based systems mostly target general musculoskeletal care or the knee. In Singapore, uptake is further limited by data-protection rules and out-of-pocket costs ([Appendix A.5](#a5-use-in-singapore-from-interviews)). None describes showing patients their progress against the expected post-RCR trajectory, adapting exercises to daily routines, or giving RCR-specific guidance on pain.

### 1.3 Novelty and value proposition

For patients recovering from RCR who struggle to keep up their home exercises, ReMotion is a home rehabilitation solution that helps them exercise regularly, correctly and at a clinically appropriate pace. Built around the post-RCR recovery phases, it offers short sessions that fit into daily routines, feedback on technique, and progress tracked against the expected recovery trajectory. ReMotion also gives physiotherapists a summary of progress between visits, saving consultation time. For the health system, better adherence could reduce stiffness-related delays and the number of patients referred back to physiotherapy ([Appendix B, Theme 7](#b4-findings-by-theme)).

ReMotion's novelty lies in supporting the shoulder after RCR in a way that fits around patients' busy lifestyles. The closest solution in Singapore, ATLAS, jointly developed by SingHealth and Rebee Health, covers multiple conditions, and does not describe adapting exercises to a patient's working day (SingHealth Community Hospitals, 2024; Ministry of Health Singapore, 2026; [Appendix A.6](#a6-gaps-against-our-specifications)). This may suit their current patients, who are likely to be still on hospitalisation leave. RCR rehabilitation, however, lasts months, and adherence falls once patients return to work ([Appendix B, Theme 1](#b4-findings-by-theme)). ReMotion therefore aims to break prescribed exercises into micro-sessions, which we will evaluate in Semester 2 ([Appendix F](#appendix-f-semester-2-prototypes)). It also guides patients on acceptable pain and shows their progress against the expected post-RCR trajectory, which none of the solutions we reviewed describes.

### 1.4 Design specifications

| ID | Specification | Justification |
|---|---|---|
| S1 | The solution tells patients whether they are performing exercises correctly, agreeing with a physiotherapist's rating of the same repetitions at least 80% of the time. | Technique is checked only in session; 8/10 physiotherapists reported technique problems ([Appendix B, Theme 2](#b4-findings-by-theme)). |
| S2 | The solution shows patients how they are progressing, so that at least 4 of 5 test participants can correctly say whether they are on track. | Patients stop once they feel "good enough" ([Appendix B, Theme 3](#b4-findings-by-theme)); seeing progress was the most wanted support (5/6; [Appendix C](#appendix-c-patient-survey)). |
| S3 | The solution fits into patients' schedules, taking no more time than their currently prescribed exercises, with set-up taking under 2 minutes. | Time was the most reported barrier; physiotherapists improve adherence by fitting exercises into routines ([Appendix B, Theme 1](#b4-findings-by-theme); [Appendix C](#appendix-c-patient-survey)). |
| S4 | The solution tells patients which pain is acceptable and when to progress, and never prompts movement beyond the range permitted for their rehabilitation phase. | Fear of pain was raised by 7/10 physiotherapists ([Appendix B, Theme 4](#b4-findings-by-theme)), and 4/6 survey respondents wanted to feel safe ([Appendix C](#appendix-c-patient-survey)). |

## 2. Methodology / Concept Development

### 2.1 Design Questions and Ideation

Based on the rehabilitation barriers identified through stakeholder interviews and patient surveys (Section 1.2), the underlying contributing factors were translated into “How Might We” design questions to guide our subsequent concept generation (Appendix D.1). The generated concepts were then organised using the Approach–Concept–Embodiment (ACE) framework, as they progress from broader strategies to specific ideas and potential implementations. For instance, under the 'Movement tracking' and 'Self-guided learning' approaches, we can potentially develop a camera-based sensor to track movements or a community forum or online resource library for patients to seek clarifications. The main approaches across the four identified problem areas are summarised below, with the complete ACE framework provided in [Appendix D.2](#d1-overall-ace-framework-for-concept-generation).

| Main Problem / Identified barriers | Main Approaches explored | Sample Ideas |
|---|---|---| 
| Uncertainty about technique | Movement tracking, Feedback provision, Assisted movement, Self-guided learning | VR/Wearables/Camera-based sensors, User-controlled exoskeleton, pre-recorded exercise videos |
| Misjudging progress | (Rehab) Progress visualisation, Scoring System, Regular reviews | Graphical visualisation markers, Telerehab remote evaluation, monthly reviews by PT |
| Lack of time and discipline | Rewards and incentives, Social support, Gamification, Micro-rehab exercises, Integration into daily routines | Vouchers, group PT sessions, online communities |
| Pain and fear of movement | Patient pain scoring, Pain detection, Answering patients' questions | Personal survey/questionnaire, AI-based companion |

### 2.2 Concept Screening & Selection

A preliminary screening was conducted to narrow the broad range of generated ideas according to their anticipated development and implementation feasibility. They were classified based on their potential feasibility and complexity when developing their prototypes. The table below summarises the concepts that were categorised accordingly, with the complete screening results provided in [Appendix D.3](#d2-overall-concept-screening-categorisation). 'Out-of-scope' ideas were not considered for further prototyping development, while we focused on 'Easy' and 'Feasible' ideas to build our prototype.

| Screening category | Summarised Ideas |
|---|---|
| Easy | Pre-recorded exercise videos, patient progress/evaluation graphs, goal setting and reminders, channel for feedback and support, micro-rehab exercises |
| Feasible | Camera-based movement tracking, wearable motion sensors, automated progress summaries, gamified incentives |
| Challenging | AI rehabilitation companion, robotic exoskeleton, AI-suggested exercises integrated into daily activities, group physiotherapy sessions, Tele-rehab |
| Out of scope | Pain detection, Walk-in PT clinic, patient self-reflections, scanning device to track Range of Motion |

Following preliminary screening, the shortlisted approaches and ideas were combined into four initial solution concepts: a digital rehabilitation coach, micro-rehab-based wearable, camera-based ROM tracking and gamified rehabilitation (Appendix D.4). They were evaluated against S1–S4 and substantial overlap was identified across the concepts, particularly in exercise flexibility, objective movement assessment, progress tracking and physiotherapist review. Rather than developing four separate solutions, we therefore converged their complementary features into one integrated 'ReMotion' concept with further prioritisation based on stakeholder needs, unmet market gaps and technical feasibility. We amended our final solution based on feedback from interim presentation.

The features include: Feedback Provision, Micro-Rehab Exercises, and Rehabilitation Progress Tracking. These concepts were prioritised for their potential to address the rehabilitation barriers identified through preliminary research, stakeholder interviews and observations of PT sessions. They also offer opportunities to support independent home rehabilitation without requiring continuous physiotherapist supervision and unlike more resource-intensive approaches such as robotic assistance or AI-based rehabilitation companions, these concepts could be explored through relatively accessible prototyping methods, such as wearable or camera-based ROM tracking. Their suitability was then assessed against the design specifications (S1–S4) using a needs-criteria evaluation matrix as shown below. Further evaluation on our final solution can be found in Appendix D.4

| Design specification (Identified barriers) | Feedback Provision | Micro-Rehab Exercises | Rehabilitation Progress Tracking |
|---|:---:|:---:|:---:|
| S1 (address uncertainty of technique) | 2 | 1 | 1 |
| S2 (address misjudging of progress) | 1 | 1 | 2 |
| S3 (address lack of time & discipline) | 0 | 2 | 1 |
| S4 (address pain & fear of movement) | 2 | 0 | 0 |
| **Average Score** | **1.25** | **1.0** | **1.0** |

Scoring: 0 = Does not meet criterion; 1 = Meets criterion; 2 = Exceeds criterion.

Based on the needs-criteria evaluation, 'Feedback Provision' showed the strongest alignment with our design specifications, particularly in providing exercise technique feedback and guiding rehabilitation. 'Rehabilitation Progress Tracking' was also identified as a promising complementary concept, allowing patients to better understand their recovery and providing relevant information for physiotherapists. Although 'Micro-Rehab exercises' scored similar to 'Progress tracking', it requires clinical validation with PT/clinicians to implement micro-rehab exercises into patients' daily routines, which we plan for future prototyping phases. Therefore, feedback provision and progress tracking were initially prioritised for further development and prototyping to assess their technical feasibility and usability before refining them further.


## 3. Fabrication of Prototypes

### 3.1 Questions the prototypes will answer

Following concept screening and evaluation (Section 2), prototyping questions were developed around the two selected concepts (feedback provision and progress tracking). Three prototypes were identified to address key uncertainties: a progress-tracking interface (P1) to assess patients' interpretation of recovery information, an exercise-session workflow (P2) to evaluate usability and setup burden, and a camera-based movement-tracking test (P3) to investigate the feasibility of objectively measuring shoulder movement. These prototypes were selected to examine individual functions before integrating them into a more comprehensive rehabilitation system. Their respective objectives and associated design specifications are summarised below.

| Design Question | Proposed Prototype | ID | Type | Spec |
|---|---|:---:|:---:|:---:|
| How should rehabilitation progress be visualised so that first-time users can easily understand it? | Progress tracker | P1 | PoC | S2 |
| How can we help patients recognise when their recovery is behind expectations, even if they feel well or are improving? | Progress tracker | P1 | PoC | S2 |
| How should a home rehabilitation exercise session be structured from start to finish? | Exercise session flow | P2 | PoC | S3 |
| How can we make each step of the exercise session intuitive and minimise difficulties for first-time users? | Exercise session flow | P2 | PoC | S3 |
| How accurately can phone-based pose estimation measure shoulder angles compared with a manual reference? | Camera tracking test | P3 | PoP | S1 |
| How do camera positioning and shoulder angles affect measurement accuracy? | Camera tracking test | P3 | PoP | S1 |

**Note:** PoC - Proof of Concept, PoP - Proof of Principle

Prototypes that need patients or clinicians are planned for Semester 2 ([Appendix F](#appendix-f-semester-2-prototypes)).

### 3.2 Prototypes for the interim stage

The prototypes are in the [prototypes](prototypes) folder of this repository, and its [README](prototypes/README.md) explains how to run each one. We built them with AI assistance (Claude Code). P1 and P2 are web pages that run in a phone browser without installation, published as links for testing: [P1](https://claude.ai/artifact/6eKZh5YK9Trb4vgazCfDg2) and [P2](https://claude.ai/artifact/MCof3qxjA9kXrffwU7wZJs).

- **P1, progress tracker** ([source](prototypes/p1_progress_tracker/index.html)). A one-screen mock-up plotting a fictional patient's shoulder range of motion against an expected recovery band, linked to a personal goal such as reaching a high shelf. Three versions show a patient who is ahead, on track, and feeling well but behind, the last recreating the point around three months when patients stop ([Appendix B, Theme 3](#b4-findings-by-theme)). They are labelled only as Screens 1–3, so the labels do not give away the answer. The recovery band is illustrative, not clinical data, because this test is about whether the chart can be read.
- **P2, exercise session flow** ([source](prototypes/p2_session_flow/index.html)). A clickable mock-up of one session: choosing the exercise, seeing instructions, setting up the phone, doing the repetitions, reporting pain and viewing the result. Two placeholder exercises use animated figures, and each animation cycle counts as one repetition. The published link uses a test photo to check framing, because the platform does not allow a live camera view.
- **P3, camera tracking test** ([source](prototypes/p3_camera_tracking/measure_angle.py)). A Python script that analysed phone video with MediaPipe Pose, an open-source pose-estimation tool that locates body landmarks in video (Bazarevsky et al., 2020). For each clip, it calculated the shoulder angle from the shoulder, elbow and hip landmarks, took measurements across frames during holding phase and reported the mean error against the reference angle. Team members raised an arm to reference angles marked with a protractor on a wall chart.

## 4. Testing

### 4.1 Purpose and scope

| ID | Method | Participants | What we record | Reference point |
|---|---|---|---|---|
| P1 | Task-based walkthrough | 9 stand-in participants (5 planned) | What participants say each version means and what they would do next | At least 4 of 5 correctly state whether the patient is on track (provisional; S2) |
| P2 | Task-based walkthrough | 8 stand-in participants (5 planned) | Steps completed unaided; where participants hesitate; time taken | Set-up under 2 minutes (provisional; S3) |
| P3 | Technical measurement | 1 team member | Difference between measured and reference angle, in degrees | Mean error within 5°-10° (Backed by interviews with PT) |

### 4.2 Interim tests: P1–P3

**P1 and P2.** We tested the prototypes with nine participants, A to I. The sessions followed these steps:

1. **P1:** participants viewed the three screens and said what each one meant.
2. **P2:** participants worked through one or both exercises, from choosing an exercise to viewing the result.

The facilitator stepped in when a participant needed help. All sessions and comments were audio-recorded and transcribed ([Appendix E](#appendix-e-test-session-findings) summarises them).

**P3.** For P3, one healthy team member performed right-arm shoulder flexion towards three manually established reference angles (50°, 90° and 120°), with three trials per angle. Each movement was recorded from a side-view camera, with the arm held at the target position for approximately three seconds before lowering. The videos were processed using the adapted MediaPipe-based script, and measurements during the holding phase were extracted to obtain a representative angle for each trial. These were subsequently compared against the corresponding reference angles to evaluate preliminary measurement agreement. All results are documented in Appendix E.

## 5. Analysis

### 5.1 Findings

We tested P1 and P2 with nine participants. Five key findings emerged, and [Appendix E](#appendix-e-test-session-findings) sets out what each participant said and did.

**Progress tracking (S2).** The chart could be read, but only 6 of the 8 participants (75%) who commented on each screen said that the Screen 1 patient was behind, short of the provisional target of 4 of 5 (80%). The others followed the rising line and did not compare it with the expected range. One likely reason is that the patient's line is the boldest element on the screen, while the expected range is a pale band and nothing tells the reader what to conclude. This mirrors how patients judge recovery ([Appendix B, Theme 3](#b4-findings-by-theme)), so a rising line could reassure a patient who is falling behind. The tracker should state plainly where the patient stands.

**Knowing what to do next (S2, S4).** The chart did not tell participants how to respond. Faced with the same patient who was behind, they reached conflicting conclusions: to exercise more, that they might be overexerting, or to see the doctor. A patient ahead of the expected range could also conclude that they need less exercise, the early stopping physiotherapists describe ([Appendix B, Theme 3](#b4-findings-by-theme)). Status also carried an emotional charge: one participant said that being behind might discourage them because they did not know why, and felt "a bit superior" when ahead. Each status needs a next step set by the physiotherapist, and being ahead must not suggest that the programme can stop.

**Guidance during exercise (S1, S3).** Some participants appeared to assume that the screen was following them, which left them unsure whether they were exercising correctly. The set-up step implies that the phone will watch them, and nothing on the exercise screen corrected this. Participants also wanted to know whether their form was right, which a repetition count cannot tell them. One participant added that a fixed animation could leave them feeling rushed, especially when moving more slowly because of pain. A better design would guide patients through each movement and wait for them to do it correctly, instead of playing the exercise automatically and counting repetitions.

**Pain (S4).** The pain score alone did not guide participants: they were unsure what a score meant or when to stop, and tended to favour the less painful exercise. They wanted the app to say when to stop and to note pauses, which the prototype does not do. The design should explain pain scores using a range set by the physiotherapist, and share pain and pauses with the physiotherapist.

**Set-up (S3).** Set-up was observed with only two participants: one took about 3 minutes, over the 2-minute target, and the other skipped it because the exercise ran regardless. This matches the positioning hassle reported with a previous system ([Appendix A.5](#a5-use-in-singapore-from-interviews)), and could add a burden when time is already the most reported barrier ([Appendix B, Theme 1](#b4-findings-by-theme)). The lack of a live view probably added to the time taken, so this is a warning, not a measure of a finished design. The design should simplify phone placement, show a live preview, and check framing before the exercise starts.

For P3, it was observed that the opensource code (from MediaPipe library) was generally able to provide relatively precise & consistent measurements from videos. Thus, it is able to measure ROM angles which aligns with S1 to an extent. The table below a sample (from trial 3) of how the readings are visualised in a graphical format. The graphs showed increasing angles during arm elevation, relatively stable measurements during the holding phase, and decreasing angles when lowering.

| Reference Angle | Graph |
|---|---|
| 50°  | <img width="512" height="203" alt="image" src="https://github.com/user-attachments/assets/fedb4fbc-d6ae-4569-addd-40b48fa374ca" /> |
| 90° | <img width="512" height="250" alt="image" src="https://github.com/user-attachments/assets/d0d4f257-6059-454e-a47e-36e1d195fa74" /> |
| 120° | <img width="512" height="226" alt="image" src="https://github.com/user-attachments/assets/5f0ba9da-8ddb-4fd6-add2-cd91176d035b" /> |

The table shows the average measurements compared against the respective reference angles (up to 3 d.p.). The collated readings were estimated from the holding phase from the raw data and were shown to be relatively consistent. Errors are small relative to our proposed 5–10° threshold.

| Reference angle/° | Trial 1/° | Trial 2/° | Trial 3/° | Mean Angle/° | Error for each trial/° | Mean Absolute Error/° |
|---|---|---|---|---|---|---|
| **50** | 51.211 | 49.808 | 49.452 | **50.157** | +1.21, −0.19, −0.55 | 0.65 |
| **90** | 87.675 | 88.283 | 90.547 | **88.835** | −2.33, −1.72, +0.55 | 1.53 |
| **120** | 121.139 | 118.70 | 120.944 | **120.261** | +1.14, −1.30, +0.94 | 1.13 |

### 5.2 Methods and validity

For P1 and P2, the sessions were audio-recorded and transcribed by an AI tool. We grouped each participant's comments and actions into findings, compared the participants (Appendix E), and compared the findings with our interviews where relevant (Section 5.1). Durations were estimated from recording timestamps. These findings are early indications, not conclusions. Since our participants are not patients, the sessions cannot show whether patients find either prototype useful.

For P3, videos of the member was taken and uploaded to the laptop to run through the opensource code. Prior to that, reference angles were estimated by measuring arm movement using protractor and ruler. However, it should be noted that the resulting measurements were compared against a protractor reference without established clinical accuracy and still lacks ability to detect incorrect forms. Additionally, the script is only able to assess movements and joints closest to camera and within 2D space.

## 6. Discussion of Problems and Project Plan

### 6.1 Problems & Potential approaches

When testing P2, the platform used to publish the prototype did not allow a live camera view, so participants checked their framing with a still photo instead. Because the exercise also played whether or not the phone was in position, set-up could be skipped, and set-up time was measured for only one participant (about 3 minutes). The S3 target of under 2 minutes therefore remains untested. In Semester 2, P2 will be hosted on a page that allows camera access, such as GitHub Pages, and the exercise will not start until framing is confirmed.

When prototyping P3, the original source code had to be adapted to introduce 0.1-second measurement intervals to reduce continuous frame-by-frame readings that generated excessive data. Raw readings were only obtained in CSV format and thus, data had to be manually translated into graphical representation for better visualisation. In order to ensure script was compatible and suitable for prototyping, preliminary testing was done (with arm movement of 90°) to verify the outputs obtained.

### 6.2 Limitations & Future mitigations

For our overall analysis, all 3 prototypes demonstrated a level of basic functionality and feasibility with our user (participants), although limitations did emerge during our prototyping process. Only a small group of users were tested on which may not be representative of our target population. However, we acknowledge these limitations and planned some mitigations for future prototyping plans as shown in the table below. 

| Prototype | Potential Problems/Limitations | Future Mitigations |
|---|---|---|
| **P1** | - Different interpretations of results and understanding of future steps to take (from user POV)<br>- Assumption of linear progress being the right progress over time.<br>- User responses assessed via audio recordings | - Add clearer recovery-status indicators, explanations of expected ranges, and PT-approved guidance on next steps.<br>- Ensure that users are clear about their progress before advancing to the next stage.<br>- In-person testing (with patients ideally) |
| **P2** | - Positioning the phone was challenging (unless recorded with assistance).<br>- Some features could be skipped, making it difficult to ensure that users were performing exercises as instructed. | - Simplify phone/device setup.<br>- Add visual positioning guidance.<br>- Integrate movement detection before claiming repetitions are completed. |
| **P3** | - Difficulty capturing user positioning and accurately identifying ROM if the user is not positioned correctly.<br>- Inaccuracy of physical reference angles.<br>- Lack of live measurements.<br>- an uninjured person, side-on view only.<br>- no lighting, clothing or distance variation.<br>- no PT input/assessment | - Use a goniometer to establish reference angles.<br>- Upgrade the source code to support live measurements and account for reference points/user positioning.<br>- Consider testing in other conditions.<br>- Consult with PT on assessment |

### 6.3 Project Prototyping Plan & Timeline

Building upon the findings from P1–P3, subsequent development will prioritise adaptive micro-rehabilitation scheduling and corrective exercise feedback, supported by ROM measurement and progress tracking. Initial activities will focus on validating clinical requirements and technical feasibility, followed by parallel feature development, integration and iterative testing. Progression between development phases will depend on the ability of each component to satisfy relevant design specifications, with further refinement guided by physiotherapist and user feedback. The proposed timeline and resources are summarised below. 

| Activity / Prototype | Resources Required | Nov 2026 (W1–4) | Dec 2026 (W5–8) | Jan 2027 (W9–12) | Feb 2027 (W13–16) | Mar 2027 (W17–20) |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **Adaptive micro-rehabilitation scheduling** — Generate short exercise sessions based on patients' availability, location and PT-prescribed plans. | App prototype, sample exercise prescriptions, scheduling algorithm, developers, PT consultation, patient input | █ W1–4 | █ W5–6 | | | |
| **Camera/sensor-based movement tracking** — Assess ROM measurement accuracy under different camera positions, lighting and movements, and compare it with sensor-baseed (IMU) measurement. | Smartphone, tripod, MediaPipe/OpenCV or other open-source tools, goniometer, IMU, 5–10 healthy volunteers | █ W1–4 | █ W5–7 | | | |
| **Real-time corrective exercise feedback** — Detect technique errors and provide actionable visual/audio corrections. | Pose-estimation software, exercise videos, developers, 1–2 PTs to define and evaluate technique errors | | █ W5–8 | █ W9–12 | █ W13 | |
| **Patient usability and progress tracking** — Assess exercise-session setup, navigation and interpretation of rehabilitation progress. | Figma/web prototypes, smartphones, 5–8 participants, questionnaires, task-based testing | | █ W5–8 | █ W9–10 | | |
| **Clinician-approved reassurance and safety guidance** — Develop rehabilitation-phase-specific guidance and symptom escalation rules. | PTs/clinicians, postoperative rehabilitation protocols, symptom scenarios, rule-based prototype | | █ W7–8 | █ W9–12 | █ W13 | |
| **Patient progress summary for PTs** — Consolidate ROM, adherence and patient-reported outcomes into a concise report. | Dashboard mock-up, simulated patient data, developers, 2–3 PTs for review | | | █ W10–12 | █ W13–14 | |
| **System integration** — Combine selected features into one functional prototype. | Integrated prototype, developers, smartphones, PT consultation | | | | █ W13–16 | █ W17–18 |
| **Integrated usability and technical evaluation** — Test selected functions against S1–S5 where feasible. | Integrated prototype, volunteers or approved patient participants, PTs/clinicians, evaluation protocols | | | | | █ W17–20 |

**Legend:** █ = Planned activity period; W = Project week.

## 7. Conclusion
In conclusion, we have identified four key barriers during our project investigation: (1) time constraints, (2) uncertainty about exercise technique, (3) difficulty assessing recovery progress, and (4) pain-related concerns. Based on these barriers, we generated some concepts and screened them based on feasibility and technical complexity, which resulted in our final solution focusing on feedback provision, progress tracking,  micro-rehab exercises. Then, we conducted initial prototyping on the former two features and yielded results that demonstrated basic functionality in progress visualisation, exercise guidance, phone-based ROM tracking, although we noted some limitations with the methods we tested. In our next step, we hope to reiterate and further refine our prototypes to develop a more clinically meaningful and suitable home rehabilitation solution.

## 8. Individual Contributions

| Team member | Contribution |
|---|---|
| Raghavi | Wrote Sections 2, 6 and 7 and the P3 parts of Sections 4 and 5; tested prototype P3  |
| Phyllis | Wrote Sections 1 and 3 and the P1 and P2 parts of Sections 4 and 5; built prototypes P1 and P2 and ran their test sessions |

## References

Bazarevsky, V., Grishchenko, I., Raveendran, K., Zhu, T., Zhang, F., & Grundmann, M. (2020). *BlazePose: On-device real-time body pose tracking*. arXiv. https://doi.org/10.48550/arXiv.2006.10204

Burns, D., Boyer, P., Razmjou, H., Richards, R., & Whyne, C. (2021). Adherence patterns and dose response of physiotherapy for rotator cuff pathology: Longitudinal cohort study. *JMIR Rehabilitation and Assistive Technologies, 8*(1), e21374. https://doi.org/10.2196/21374

Ministry of Health Singapore. (2026, July 11). *Speech by Mdm Rahayu Mahzam, Minister of State, Ministry of Digital Development and Information & Ministry of Health, at the Singapore International Physiotherapy Congress 2026*. https://www.moh.gov.sg/newsroom/speech-by-mdm-rahayu-mahzam--minister-of-state--ministry-of-digital-development-and-information---ministry-of-heatlh-at-the-singapore-international-physiotherapy-congress-2026--11-july-2026--9am/

Sambandam, S. N. (2015). Rotator cuff tears: An evidence based approach. *World Journal of Orthopedics, 6*(11), 902. https://doi.org/10.5312/wjo.v6.i11.902

Simon, L. M., Nguyen, V., & Ezinwa, N. M. (2023). Acute shoulder injuries in adults. *American Family Physician, 107*(5), 503–512. https://www.aafp.org/afp/2023/0500/acute-shoulder-injuries

SingHealth Community Hospitals. (2024, May 13). *AI-assisted physiotherapy system*. https://www.singhealth.com.sg/sch/about-sch/news/news-release/2024/ai-assisted-physiotherapy-system.newsdetails

Sripathi, P., & Agrawal, D. K. (2024). Rotator cuff injury: Pathogenesis, biomechanics, and repair. *Journal of Orthopaedics and Sports Medicine, 6*(4). https://doi.org/10.26502/josm.511500167

## Appendices

### Appendix A: Review of existing solutions

#### A.1 Method

We identified 17 existing solutions through searches of company websites, news releases and published trials, supplemented by tools mentioned in our stakeholder interviews (Appendix B). We grouped them into direct competitors, which support home rehabilitation through software or sensors, and adjacent solutions, which are physical, robotic or VR equipment used mainly in specific phases or in clinics. Features were taken from each solution's official website, news release or published trial. A dash (–) means the feature was not described in the information we reviewed, not that it is definitely absent.

#### A.2 Direct competitors: profiles

| Solution | Type | Main buyer | Body region | Price | Stage |
|---|---|---|---|---|---|
| Medbridge | Digital exercise platform | Clinicians, clinics, hospitals | Multiple | Individual $100–389/yr; small business $209–369/yr | Commercial; used in a Singapore public hospital |
| Physitrack | Digital exercise platform | Physiotherapists, clinics | Multiple | $334.69/yr per clinician; free app for patients | Commercial |
| PhysioBuddy | Digital exercise platform | Physiotherapists | Multiple | – | Used by some physiotherapists at SGH |
| Rebee Health | Wearable sensors and app | Healthcare providers | Multiple, including post-RCR | Paid out of pocket by patients (Appendix B) | Commercial; used in a Singapore public hospital for knee and hip |
| Kinexcs (KIMIA) | Wearable sensors and app | Hospitals, orthopaedic providers | Mainly knee | – | Commercial |
| OrthoRPM | Connected devices and app | Rehabilitation providers, orthopaedic practices | Multiple, including shoulder | – | Commercial |
| Sword Health | Camera and AI-guided digital physiotherapy | Employers, health plans | General MSK | Through employer or health plan | Commercial |
| Hinge Health | Camera-guided digital physiotherapy | Employers, health plans | General MSK | $0 to eligible members | Commercial |
| ANAPA | Digital rehabilitation and shoulder assessment | Post-RCR patients, clinicians | Shoulder, post-RCR | – | Research (24-week pilot trial) |
| UINCARE Home+ | Augmented-reality home rehabilitation | Hospitals, rehabilitation providers | Shoulder, including post-RCR | – | Clinical trial; commercial availability unconfirmed |
| ATLAS | Wearable sensor and apps | Community hospitals | Multiple conditions | – | In use at three Singapore community hospitals; co-developed with Rebee Health |

#### A.3 Direct competitors: features

| Solution | Guided exercises | Real-time technique feedback | ROM or strength tracking | Adherence tracking | Remote clinician monitoring | Pain or fear support |
|---|---|---|---|---|---|---|
| Medbridge | ✓ | – | ✓ | ✓ | ✓ | – |
| Physitrack | ✓ | – | – | ✓ (self-reported) | ✓ | – |
| PhysioBuddy | ✓ | – | – | – | – | – |
| Rebee Health | ✓ | ✓ | ✓ | ✓ | ✓ | – |
| Kinexcs (KIMIA) | ✓ | ✓ | ✓ | – | ✓ | – |
| OrthoRPM | ✓ | – | ✓ | ✓ | ✓ | – |
| Sword Health | ✓ | ✓ | ✓ | – | ✓ | ✓ |
| Hinge Health | ✓ | ✓ | ✓ | – | ✓ | ✓ |
| ANAPA | ✓ | – | ✓ | – | ✓ | – |
| UINCARE Home+ | ✓ | ✓ | ✓ | ✓ | ✓ | – |
| ATLAS | ✓ | ✓ | ✓ | ✓ | ✓ | – |

#### A.4 Adjacent solutions

| Solution | Type | Role in rehabilitation | Why adjacent |
|---|---|---|---|
| KineQuantum | VR rehabilitation | Gamified exercises, biofeedback, support for fear of movement | Used in clinics and home visits, not unsupervised home practice |
| Kinetec Centura | Continuous passive motion machine | Moves the shoulder passively through a set range | Early passive phase only; clinical equipment |
| Breg ARC Dynamic | Post-operative brace with passive-motion reel | Supports the shoulder and allows prescribed passive movement | Early phase only |
| ShoulderSphere | Strengthening device | Rotator cuff strengthening | Late phase; aimed at athletes and trainers |
| Tyromotion Diego | Robotic arm system | Assisted movement and VR task practice | Hospital and rehabilitation-centre equipment |
| ARTICARES H-Man | Robotic upper-limb system (developed in Singapore) | Adaptive resistance, gamified exercise, remote monitoring | Mainly used in institutions, with selected home settings |

#### A.5 Use in Singapore (from interviews)

- **Medbridge Go** is used in one public hospital (PT9). Because its servers are outside Singapore, data-protection rules mean clinicians can see only whether patients log in, not whether they complete their exercises.
- **Rebee Health** has been used in the same hospital since March 2026 for knee and hip patients. Patients pay out of pocket, uptake has been 29 patients, and it has not yet been used for shoulder patients (PT9).
- **Anycare** was beta-tested in a public hospital. Positioning for joint-angle measurement was a hassle for patients, and strength could not be tested remotely (PT4).
- In practice, the most common take-home materials remain **printed exercise sheets and videos recorded on patients' phones** (PT1, PT6, PT10, P3).

#### A.6 Gaps against our specifications

| Need | Addressed by | Remaining gap |
|---|---|---|
| Feedback on technique (S1) | Sensor- and camera-based systems (Rebee Health, ATLAS, Kinexcs, Sword Health, Hinge Health, UINCARE Home+) | Digital exercise platforms give no technique feedback. Most sensor systems target general MSK care or the knee, and in Singapore their use is limited by out-of-pocket cost and set-up effort |
| Seeing progress (S2) | Most direct competitors track ROM or strength | Tracking is described mainly as clinician dashboards. ATLAS gives patients feedback on progress towards their rehabilitation goals, but none of the solutions reviewed describes showing patients their progress against the expected post-RCR trajectory |
| Fitting into schedules (S3) | Exercise reminders (Medbridge, Physitrack) | None describes adapting the programme to patients' daily routines |
| Saving physiotherapists' time (S4) | PhysioBuddy (reducing admin), Medbridge (EMR integration), ARTICARES H-Man (automatic reports) | Local data-protection rules limit what overseas platforms can share with clinicians |
| Designed for post-RCR | Rebee Health (among other conditions), ANAPA, UINCARE Home+, Breg ARC Dynamic | ANAPA and UINCARE Home+ remain at research stage; Breg ARC Dynamic covers the passive phase only |
| Guidance on pain | Sword Health, Hinge Health (general MSK pain management), KineQuantum (fear of movement) | No solution reviewed offers RCR-specific guidance on acceptable pain and when to progress |

[← Back to Section 1](#1-objective-scope-and-context) | [↑ Back to contents](#table-of-contents)

### Appendix B: Summary of stakeholder interviews

#### B.1 Method

We conducted semi-structured interviews with 6 patients, 10 physiotherapists and 3 orthopaedic surgeons between August and October 2026. Interviews were held in person, by video call or by phone. Each interview was recorded and transcribed, or documented in detailed notes, and summarised in a structured record. We then grouped findings into themes and counted how many participants in each group raised each theme, whether unprompted or in response to a question. Counts indicate how widely a view was held, not its statistical prevalence. Participants are anonymised below; quotations are verbatim from transcripts, translated from Mandarin where marked.

#### B.2 Participants

| ID | Role and setting | Relevant experience | Date and mode |
|---|---|---|---|
| P1 | Patient, female, 60s | ~6 months after RCR; public physiotherapy | 25 Sep 2026, phone (Mandarin) |
| P2 | Patient, male | ~4 months after RCR; private physiotherapy | 17 Sep 2026 |
| P3 | Patient, male, 50s | RCR on both shoulders, most recently Aug 2026; public physiotherapy | 16 Sep 2026, phone |
| P4 | Patient, male | ~1.5 years after RCR; public then private physiotherapy | 16 Sep 2026, phone |
| P5 | Patient, female, 40s | ~1 year after RCR; stopped physiotherapy after 3–4 sessions | 16 Sep 2026, phone |
| P6 | Patient, female, 40s | Conservative (non-surgical) management; private physiotherapy | 25 Sep 2026 |
| PT1 | Physiotherapist, private clinic | Previously public inpatient | 31 Aug 2026, in person |
| PT2 | Physiotherapist, private clinic | Previously community and nursing-home care | 3 Sep 2026, video call |
| PT3 | Physiotherapist, public hospital | Inpatient, outpatient MSK and home therapy | 5 Sep 2026 |
| PT4 | Physiotherapist, private clinic | ~5.5 years in a public hospital, latterly leading the post-operative shoulder service | 8 Sep 2026 |
| PT5 | Physiotherapist, private clinic | Shoulder specialist; previously public sector | 17 Sep 2026, in person |
| PT6 | Physiotherapist, public hospital | Outpatient MSK, 2 years | 17 Sep 2026 |
| PT7 | Physiotherapist, private clinic | 12 years in a public hospital shoulder team | [date] |
| PT8 | Physiotherapist | 13–15 years in a public hospital and polyclinic; 1 year private | [date] |
| PT9 | Senior physiotherapist, public hospital | Sports and orthopaedic outpatient team | 29 Sep 2026 |
| PT10 | Physiotherapist, polyclinic | Community outpatient MSK | 9 Oct 2026 |
| S1 | Orthopaedic surgeon, public hospital | Consultant, shoulder and elbow | 8 Sep 2026, video call |
| S2 | Orthopaedic surgeon, public hospital | Senior consultant, sports and shoulder | 22 Sep 2026, video call |
| S3 | Orthopaedic surgeon, public hospital | Shoulder surgeon; project clinical mentor | 3 Oct 2026, video call |
| O1 | Observation, private clinic | Physiotherapy session with a post-operative shoulder patient | 1 Sep 2026, in person |

#### B.3 Interview topics

Guides were adapted to each stakeholder group.

- **Physiotherapists:** caseload and patient profile; rehabilitation phases and session frequency; how home-exercise adherence is checked; reasons for non-adherence and drop-off; pain and fear of movement; communication with surgeons; take-home materials and digital tools; information they would want between visits.
- **Surgeons:** patient selection and expectation-setting; rehabilitation timelines; visibility of patients after referral to physiotherapy; outcome measurement; payment and funding.
- **Patients:** recovery journey since surgery; physiotherapy access; how often they did home exercises and what got in the way; take-home materials; experience of pain; recovery goals.

#### B.4 Findings by theme

**Theme 1: Time and competing commitments** (7/10 physiotherapists, 4/6 patients)

Adherence is highest during hospitalisation leave and falls when patients return to work (PT2, PT8). Working patients reported skipping exercises because of work or travel (P2, P5, P6) or when busy (P3). Attending appointments is also harder for working patients, because physiotherapists cannot issue medical certificates and public clinics offer few out-of-hours slots (PT8, PT10, P1). Experienced physiotherapists tailor prescriptions to the time patients realistically have, often 1–3 exercises that fit into daily routines (PT2, PT8).

> "Time is the primary barrier, even for the PT herself." (PT3, interview notes)
>
> "I can't book your physio because your physio is so busy. And when you have a slot, I can't make it — I have to take leave for physio." (P1, translated)

**Theme 2: Uncertainty about technique** (8/10 physiotherapists, 3/6 patients, 2/3 surgeons)

All physiotherapists check technique by asking patients to demonstrate their exercises in session, and several reported that a lack of progress often reflects incorrect form rather than skipped exercises (PT1, PT3, PT6). Patients forget exercises between visits, and printed sheets are hard to follow (PT7, PT9). Patients and their families often film the physiotherapist as a workaround (S2, PT6, P3).

> "No one taught me, I don't know how to do it, I just do it anyhow. If I don't, it'll go stiff, so I move it a bit, and when it hurts I stop." (P1, translated)
>
> "Some patients may look at the image and they couldn't understand what do I need to do again." (PT9)

**Theme 3: Judging progress and when to progress** (7/10 physiotherapists)

Physiotherapists reported that patients often stop exercising or attending once they feel "good enough", typically around three months after surgery, although strength and range are not yet fully restored (PT3, PT4, PT6, PT7, PT9). Without feedback between visits, some patients repeat the same dose without progressing (PT8). One physiotherapist who shows patients their test results at every session reported that this greatly improved adherence (PT5).

> "Especially after three months they start feeling better, they don't do it as much." (PT4)
>
> "They can see their progress every single session and they are more motivated to come because of that." (PT5)

**Theme 4: Pain and fear of movement** (7/10 physiotherapists, 2/6 patients)

Patients often interpret pain as damage to the repair, stop exercising and return with stiffness (PT1, PT3, PT7). They are unsure which pain is acceptable (PT1, P3) and use pain as a signal to stop (P1, P3).

> "When there's pain, they don't dare to push." (PT9)
>
> "I feel pain with this — is that normal?" (a common question from patients, reported by PT8)

**Theme 5: Access to public physiotherapy** (6/10 physiotherapists, 2/6 patients, 2/3 surgeons)

In public hospitals, the first post-operative session is usually 1–4 weeks after surgery, and follow-up sessions are often 3–4 weeks apart (PT6, PT7, PT9). Physiotherapists described drop-off in public settings as partly capacity-driven (PT4). One patient had only one physiotherapy session after surgery and could not rebook (P1); another moved to private physiotherapy to be seen more often (P4). Capacity is unlikely to grow soon: S2 reported a long-standing limit on hiring physiotherapists in public hospitals, a national shift of rehabilitation resources towards community care, and trained physiotherapists leaving for private practice.

> "We can keep on telling the physios, hey, you must increase, increase, increase. It's not going to happen for some time." (S2)

**Theme 6: Physiotherapists' time and visibility between visits** (5/10 physiotherapists)

Physiotherapists learn about home adherence only when patients return (PT2, PT8). They would like to see how often exercises are done and whether target angles are reached (PT9, PT10), and said a summary of between-visit data would save consultation time (PT9, PT10). Public sessions last about 30 minutes (PT6, PT8, PT10), and high caseloads mean exercise supervision is sometimes delegated to therapy assistants (PT6).

> "The most important will be compliance and whether they reach the target angle." (PT9)

**Theme 7: Consequences of non-adherence** (4/10 physiotherapists, 1/3 surgeons)

The most common consequence described was secondary stiffness, which can extend recovery from about 6 to 10 months (PT3, PT9, S3). Non-adherence can delay recovery by up to 18 months (PT4), and patients who miss milestones at surgeon review are referred back to physiotherapy (PT7).

#### B.5 Estimates of adherence and drop-off

These figures are individual physiotherapists' estimates, not measured rates.

| Source | Setting | Estimate |
|---|---|---|
| PT4 | Public hospital (former) | ~50% of patients do not do home exercises; 20–30% drop out of public physiotherapy, of whom only 5–10% return |
| PT10 | Polyclinic | ~70% do home exercises as prescribed |
| PT2 | Private clinic | Working patients often fall off after returning to work (~30%) |
| PT1 | Private clinic | ~10–15% drop off, mainly when insurance coverage runs out |
| PT9 | Public hospital | 8–9 in 10 patients complete the course |
| PT5 | Private clinic | Near-complete adherence; non-adherent patients are discharged |

#### B.6 Divergent views

- **S1** reported no adherence problems among their post-operative patients, and attributed this to strict patient selection and to making a 6–9 month rehabilitation commitment a condition of surgery.
- **PT5 and PT9** reported high adherence in their settings: PT5 in a high-cost private clinic that discharges non-adherent patients, and PT9 in a public hospital where most drop-outs had already recovered.
- **PT2** noted that recovery can be similar with reduced home exercise, because daily activities can substitute for prescribed exercises.
- **PT7, PT4 and S2** cautioned against claiming that incomplete rehabilitation always causes complications. S2 reported that patients satisfied with their function despite poor objective scores do not have higher complication rates.

These views suggest that non-adherence is concentrated among working patients in settings with infrequent follow-up, rather than being universal.

[← Back to Section 1](#1-objective-scope-and-context) | [↑ Back to contents](#table-of-contents)

### Appendix C: Patient survey

#### C.1 Method

We ran an online survey of patients recovering from RCR between 7 and 13 October 2026 and received 6 responses. The survey used multiple-choice questions, including select-all and top-three questions, with optional free-text answers. Names and contact details were removed before analysis.

#### C.2 Respondents

| Characteristic | Responses |
|---|---|
| Age | 31–40 (1), 41–50 (2), 51–60 (2), 61–70 (1) |
| Gender | Male (4), female (2) |
| Employment | Full-time (5), not working (1) |
| Time since surgery | 4–19 months |
| Current physiotherapy | Weekly or more (2), about monthly (1), every 2–3 months (1), stopped (2) |
| Help with home exercises | None (5), occasional (1) |

#### C.3 Difficulties with home exercises

| Difficulty | Experienced in the last month | Among their 3 hardest |
|---|---|---|
| No time, because work or family crowded exercises out | 3 | 3 |
| Missed a physiotherapy appointment, and the next was far away or time off was not possible | 2 | 3 |
| Shoulder stayed stiff or painful, or was not recovering as hoped | 2 | 3 |
| Exercise hurt, so was afraid to push and did less | 2 | 2 |
| Could not tell whether they were improving | 1 | 2 |
| Unsure whether exercises were done correctly, and worried about making it worse | 1 | 1 |

In free text, 3 respondents named discipline as the hardest part of home exercise, and 1 said they stop when they feel pain.

#### C.4 Support wanted (top three)

| Support | Respondents |
|---|---|
| Clearly seeing how I'm progressing | 5 |
| Feeling safe that exercise won't make my pain worse | 4 |
| Easy to fit into my daily routine | 3 |
| Quick answer when something feels wrong | 3 |
| Someone keeping an eye on me | 2 |
| Recovering without clinic trips or time off | 1 |

Other things respondents found helpful were YouTube videos on their condition and daily activities after surgery, and more frequent physiotherapy appointments.

#### C.5 Key findings and limitations

- **Seeing progress and feeling safe were the most wanted forms of support**, chosen by 5 and 4 of 6 respondents. This supports specification S2 and the pain guidance in ReMotion.
- **Time was the most common difficulty**, reported by 3 of the 5 working respondents, alongside difficulty getting to appointments. This supports S3.
- **Home exercise is done alone:** 5 of 6 respondents had no help, so support needs to reach the patient directly.
- **Few respondents doubted their technique** (1 of 6), whereas physiotherapists widely reported technique problems (Appendix B, Theme 2). This suggests patients may not recognise their own errors, which supports objective technique feedback (S1).
- **Limitations:** the sample is small and self-selected, and most respondents are working men, so the results show the range of patient experiences rather than how common each one is.

[← Back to Section 1](#1-objective-scope-and-context) | [↑ Back to contents](#table-of-contents)

### Appendix D: Concept Generation & Screening

#### D.1 'How might we' Design questions & identified barriers

Problem (Section 1.2) | Root cause | Design question | Spec |
|---|---|---|---|
| Lack of time and discipline | Work and daily commitments compete with rehabilitation. Patients may lose motivation once they feel sufficiently recovered and this may lead to low adoption rate. | How might we help patients incorporate prescribed rehabilitation exercises into their daily routines and sustain engagement throughout recovery? | S3 |
| Uncertainty about technique | Patients receive limited feedback between PT appointments and PTs are only able to correct these exercises during the sessions themselves. | How might we enable patients to recognise and correct improper exercise techniques independently during the home rehabilitation phase? | S1 |
| Misjudging progress | Patients have limited access to objective information on their progress unless requested and may mistake reduced pain or improved function for complete recovery. | How might we help patients understand their rehabilitation progress and potentially recognise when further improvement is needed? | S2 |
| Pain and fear of movement | Patients sometimes do not understand that the pain/discomfort during exercise is to be expected or whether the pain they feel requires them to seek professional advice | How might we help patients handle uncertainty about exercise-related pain and potentially continue rehabilitation safely within prescribed limits? | S5 |
| PT time and visibility between visits | Home rehabilitation is largely self-managed, where PTs mostly rely on patient-reported responses and in-person reassessment.| How might we provide physiotherapists with relevant, actionable information about patients' home rehabilitation while minimising additional workload? | S4 |

#### D.2 Overall ACE Framework for concept generation

<table>
  <thead>
    <tr>
      <th>PROBLEM</th>
      <th>APPROACH</th>
      <th>CONCEPT</th>
      <th>EMBODIMENT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="15"><b>(1) Patients can't tell if they are doing the exercises correctly</b></td>
      <td rowspan="5"><b>APPROACH 1</b><br>Movement tracking and feedback</td>
      <td rowspan="2"><b>Concept 1A</b><br>Movement tracking</td>
      <td>Camera and screen or VR and sensors to track movement</td>
    </tr>
    <tr><td>Wearable sensors: EMG or gyroscope or accelerometer</td></tr>
    <tr>
      <td rowspan="3"><b>Concept 1B</b><br>Real-time feedback</td>
      <td>Pain detection: facial expression, jerking movement, patient input (verbal or haptic)</td>
    </tr>
    <tr><td>Visual or auditory or haptic feedback on what's wrong and how to adjust</td></tr>
    <tr><td>AI-related companion (like Alexa or Google Home)</td></tr>
    <tr>
      <td rowspan="5"><b>APPROACH 2</b><br>Assisted Movement</td>
      <td rowspan="2"><b>Concept 2A</b><br>Physical constraint</td>
      <td>Machine to isolate the muscle</td>
    </tr>
    <tr><td>Device to limit bending angle or ROM (physical restraint)</td></tr>
    <tr>
      <td rowspan="3"><b>Concept 2B</b><br>Physical aid</td>
      <td>Pneumatic or hydraulics driven exoskeleton for controlled movement</td>
    </tr>
    <tr><td>Pulley system to utilize unaffected hand to assist movement</td></tr>
    <tr><td>Automatic adjustable thermal sleeve to aid with cold therapy</td></tr>
    <tr>
      <td rowspan="5"><b>APPROACH 3</b><br>Self-guided Learning</td>
      <td rowspan="2"><b>Concept 3A</b><br>Video Instruction recordings</td>
      <td>Auto-recorded PT session and creation of video library for the patients to refer to</td>
    </tr>
    <tr><td>Creation of pre-recorded video exercise by the PT or other professionals</td></tr>
    <tr>
      <td rowspan="3"><b>Concept 3B</b><br>Community Based</td>
      <td>Recruit personal trainer, yoga instructor, etc. as trusted source of advice at local level</td>
    </tr>
    <tr><td>Community based-forum with PT and doctors as verified professionals to answer question</td></tr>
    <tr><td>Local PT walk-in 5 minute clinic for quick questions</td></tr>
  </tbody>
</table>



<table>
  <thead>
    <tr>
      <th>PROBLEM</th>
      <th>APPROACH</th>
      <th>CONCEPT</th>
      <th>EMBODIMENT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="14"><b>(2) Patients don't know if they are progressing</b></td>
      <td rowspan="5"><b>APPROACH 1</b><br>Visualization</td>
      <td rowspan="2"><b>Concept 1A</b><br>Diagram</td>
      <td>Diagram to show animated visualization of the actual repair</td>
    </tr>
    <tr><td>Images of MRI taken during doctors' appointments with labelling to show progress</td></tr>
    <tr>
      <td rowspan="3"><b>Concept 1B</b><br>Graph</td>
      <td>Graph to show time required to reach milestones</td>
    </tr>
    <tr><td>Graph to show patients' progress over time, and link progress with important life goals</td></tr>
    <tr><td>To be able to compare against base/normal range to show progression</td></tr>
    <tr>
      <td rowspan="5"><b>APPROACH 2</b><br>Scoring system</td>
      <td rowspan="2"><b>Concept 2A</b><br>Objective scoring</td>
      <td>PT's objective evaluations are recorded for patients to view</td>
    </tr>
    <tr><td>Automatic scoring of patients using measurements recorded from sensors</td></tr>
    <tr>
      <td rowspan="3"><b>Concept 2B</b><br>Subjective scoring</td>
      <td>PT's subjective evaluations are recorded for patients to view</td>
    </tr>
    <tr><td>Patients' own scoring of their pain/functionality</td></tr>
    <tr><td>Assistance from caregivers or family members to help with scoring</td></tr>
    <tr>
      <td rowspan="4"><b>APPROACH 3</b><br>Regular review</td>
      <td rowspan="2"><b>Concept 3A</b><br>Monthly/weekly check-ins</td>
      <td>Auto-generated monthly/weekly summaries based on recorded measurements</td>
    </tr>
    <tr><td>Telerehab and remote evaluation combined with home-based sensor data</td></tr>
    <tr>
      <td rowspan="2"><b>Concept 3B</b><br>Self-reflections</td>
      <td>Monthly reviews generated from patients' own reflections on their daily progress</td>
    </tr>
    <tr><td>Feedback from PT to assess the reviews and get back to patient (online)</td></tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>PROBLEM</th>
      <th>APPROACH</th>
      <th>CONCEPT</th>
      <th>EMBODIMENT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="25"><b>(3) Patients struggle to find time and discipline to do the full set of prescribed exercises at home</b></td>
      <td rowspan="5"><b>APPROACH 1</b><br>Rewards</td>
      <td rowspan="2"><b>Concept 1A</b><br>Monetary incentives</td>
      <td>NTUC vouchers/rebates for unlocking certain milestones</td>
    </tr>
    <tr><td>Patient deposit that is deductible (for charity) if patient not doing exercise</td></tr>
    <tr>
      <td rowspan="3"><b>Concept 1B</b><br>Non-monetary incentives</td>
      <td>Badges/recognition for good behaviour</td>
    </tr>
    <tr><td>Goal setting &amp; progress tracking</td></tr>
    <tr><td>Words of encouragement from the app as the patient do the exercise</td></tr>
    <tr>
      <td rowspan="7"><b>APPROACH 2</b><br>Social support</td>
      <td rowspan="3"><b>Concept 2A</b><br>Competition</td>
      <td>Competing with other patients on the same recovery journey (e.g. Duolingo but for rehab) | Rehab Leaderboard</td>
    </tr>
    <tr><td>Competing as a group with patients from other groups (e.g. knee)</td></tr>
    <tr><td>Competing with family/friends who are trying to keep fit</td></tr>
    <tr>
      <td rowspan="4"><b>Concept 2B</b><br>Support group</td>
      <td>Group physiotherapy:<br>- At local community centres or zones, doing PT with fellow peers<br>- In groups with other patients (e.g. group-based PT session) with little PT supervision</td>
    </tr>
    <tr><td>Online communities to share encouragement (e.g. Strava for rehab)</td></tr>
    <tr><td>Asynchronous "exercise together" see when your buddy completes the same session</td></tr>
    <tr><td>Personal rehab avatar that accompanies patient during exercises, learning their habits and mood over time; shares progress updates with family/friends (with patient's approval), so loved ones can cheer them on without patient having to explain</td></tr>
    <tr>
      <td rowspan="5"><b>APPROACH 3</b><br>Gamification</td>
      <td rowspan="2"><b>Concept 1A</b><br>Gamified rewards</td>
      <td>Unlocking certain in-app rewards when milestones are reached</td>
    </tr>
    <tr><td>Tie in with incentives to received (similar to Healthy 365 10K steps challenge etc)</td></tr>
    <tr>
      <td rowspan="3"><b>Concept 1B</b><br>Rehab as games</td>
      <td>Turn rehab exercises into mini-games with progress levels with in-game competition</td>
    </tr>
    <tr><td>Adaptive exercise difficulty "just within reach" level based on user's recent performance</td></tr>
    <tr><td>Exercises unlockable as patient reaches milestone</td></tr>
    <tr>
      <td rowspan="8"><b>APPROACH 4</b><br>Integration with daily routine</td>
      <td rowspan="3"><b>Concept 2A</b><br>Part of activities done at home/work</td>
      <td>AI to suggest how to incorporate exercises with everyday tasks, e.g. lifting and reaching for cabinet, ironing shirt, wiping table</td>
    </tr>
    <tr><td>Fidget toys but for shoulder rehab</td></tr>
    <tr><td>Using MRT or public transport handle for exercise</td></tr>
    <tr>
      <td rowspan="5"><b>Concept 2B</b><br>A way to fit into their daily schedule</td>
      <td>Camera based scanning device that tracks ROM while PT can immediately read measurements while talking with patient</td>
    </tr>
    <tr><td>Turn off alarm by doing exercise and Desktop widget reminders</td></tr>
    <tr><td>Make rehab tool feels luxurious (smooth wood, etc.) (not mundane looking medical tools)</td></tr>
    <tr><td>Micro rehab exercises (1 min each) during small windows of free time. Concept same as Anki or flashcard, to be done while MRT, waiting in queue, bored, desk job, etc.</td></tr>
    <tr><td>Snap surroundings → AI suggests rehab exercises using nearby objects; new environment, new routine each time</td></tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>PROBLEM</th>
      <th>APPROACH</th>
      <th>CONCEPT</th>
      <th>EMBODIMENT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7"><b>(4) PT spending more time reviewing notes &amp; performing documentation</b></td>
      <td rowspan="4"><b>APPROACH 1</b><br>Automated documentation for patients ROM</td>
      <td rowspan="2"><b>Concept 1A</b><br>Device that can automatically assess patient's ROM</td>
      <td>A type of scanning device that can assess ROM in 3D</td>
    </tr>
    <tr>
      <td>Home rehab sensors and patient scoring</td>
    </tr>
    <tr>
      <td rowspan="2"><b>Concept 1B</b><br>Visual assessment</td>
      <td>Camera based scanning device that tracks ROM while PT can immediately read measurements while talking with patient</td>
    </tr>
    <tr>
      <td>Audio + vision ambient scribe - PT taps to capture key measurements (e.g. ROM), auto-documented with conversation context</td>
    </tr>
    <tr>
      <td rowspan="3"><b>APPROACH 2</b><br>Recording of patients' notes</td>
      <td rowspan="2"><b>Concept 2A</b><br>A way to prescribe notes for each session</td>
      <td>AI-enabled prescriber that records details discussed in each session</td>
    </tr>
    <tr>
      <td>Assess multilingual conversations</td>
    </tr>
    <tr>
      <td><b>Concept 2B</b><br>Self-reported documentation</td>
      <td>Conversational AI intake before first visit: chatbot interviews patient in a friendly, engaging way, and sends a structured summary to the PT before the patient walks in</td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>PROBLEM</th>
      <th>APPROACH</th>
      <th>CONCEPT</th>
      <th>EMBODIMENT</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4"><b>(5) Pain and fear of movement</b></td>
      <td><b>APPROACH 1</b><br>Patient pain scoring</td>
      <td><b>Concept 1A</b><br>Subjective scoring</td>
      <td>Patients' own scoring of their pain/functionality</td>
    </tr>
    <tr>
      <td><b>APPROACH 2</b><br>Pain detection</td>
      <td><b>Concept 2A</b><br>Automatic detection</td>
      <td>Pain detection: facial expression, jerking movement, patient input (verbal or haptic)</td>
    </tr>
    <tr>
      <td rowspan="2"><b>APPROACH 3</b><br>Answering patients' questions</td>
      <td rowspan="2"><b>Concept 3A</b><br>Access to professionals</td>
      <td>Community based-forum with PT and doctors as verified professionals to answer question</td>
    </tr>
    <tr><td>Local PT walk-in 5 minute clinic for quick questions</td></tr>
  </tbody>
</table>

#### D.3 Overall Concept screening categorisation

'Easy' concepts for instance demonstrate already established technology that is relatively simple to recreate, while 'Feasible' ones may require slightly more resources or technology to develop but can be achieved. 'Challenging' concepts require vastly more resources or knowledge to validate and develop, while those under 'Out of scope' do not directly address the problems or lack feasibility. The two tables below show both the summarised and complete version of our concept screening based on this criteria.

| Screening category | Summarised concepts |
|---|---|
| Easy | Pre-recorded exercise videos, patient progress/evaluation graphs, goal setting and reminders, channel for feedback and support, micro-rehab exercises |
| Feasible | Camera-based movement tracking, wearable motion sensors, automated progress summaries, gamified incentives, AI-based prescriber (for PT) |
| Challenging | AI rehabilitation companion, robotic exoskeleton, AI-suggested exercises integrated into daily activities, group physiotherapy sessions, Tele-rehab, Auto-recorded PT sessions |
| Out of scope | Pain detection, Walk-in PT clinic, patient self-reflections, scanning device to track Range of Motion |

<table>
  <thead>
    <tr>
      <th>Problem(s)</th>
      <th>'Out of Scope' Concepts Identified</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">
        Patients can't tell if they are doing the exercises correctly
      </td>
      <td>VR and sensors to track movement</td>
    </tr>
    <tr>
      <td>Pain detection: facial expression, jerking movement, patient input (verbal or haptic)</td>
    </tr>
    <tr>
      <td>Machine to isolate the muscle</td>
    </tr>

  <tr>
      <td rowspan="2">
        Patients don't know if they are progressing
      </td>
      <td>Graph to show time required to reach milestones</td>
    </tr>
    <tr>
      <td>Assistance from caregivers or family members to help with scoring</td>
    </tr>

   <tr>
      <td rowspan="3">
        Patients struggle to find time and discipline to do the full set of prescribed exercises at home
      </td>
      <td>Patient deposit that is deductible (for charity) if patient does not do exercises</td>
    </tr>
    <tr>
      <td>Competing as a group with patients from other groups (e.g. knee rehabilitation)</td>
    </tr>
    <tr>
      <td>Competing with family/friends who are trying to keep fit</td>
    </tr>

   <tr>
      <td rowspan="2">
        PT spending more time on reviewing notes and performing documentation
      </td>
      <td>A scanning device that can assess ROM in 3D</td>
    </tr>
    <tr>
      <td>Camera-based scanning device that tracks ROM while PT can immediately read measurements during consultation</td>
    </tr>
  </tbody>
</table>


<table>
  <thead>
    <tr>
      <th>Problem(s)</th>
      <th>'Easy' Concepts Identified</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">Patients can't tell if they are doing the exercises correctly</td>
      <td>Visual, auditory or haptic feedback on what is wrong and how to adjust</td>
    </tr>
    <tr><td>Pulley system using the unaffected hand to assist movement</td></tr>
    <tr><td>Thermal sleeve to aid with cold therapy</td></tr>
    <tr><td>Creation of pre-recorded exercise videos by PTs or other professionals</td></tr>

   <tr>
      <td rowspan="5">Patients don't know if they are progressing</td>
      <td>Graph showing patients' progress over time, linked to important life goals and reference ranges</td>
    </tr>
    <tr><td>PT's objective evaluations recorded for patients to view</td></tr>
    <tr><td>Automatic patient scoring using sensor-recorded measurements</td></tr>
    <tr><td>PT's subjective evaluations recorded for patients to view</td></tr>
    <tr><td>Patients' self-reported scoring of pain and functionality</td></tr>

   <tr>
      <td rowspan="6">Patients struggle to find time and discipline to do the full set of prescribed exercises at home</td>
      <td>Badges or recognition for good rehabilitation behaviour</td>
    </tr>
    <tr><td>Goal setting and progress tracking</td></tr>
    <tr><td>Words of encouragement during exercises</td></tr>
    <tr><td>Exercises unlocked upon reaching PT-approved milestones</td></tr>
    <tr><td>Using MRT or public transport handles for exercises</td></tr>
    <tr><td>Micro-rehabilitation exercises during short periods of free time</td></tr>
  </tbody>
</table>


<table>
  <thead>
    <tr>
      <th>Problem(s)</th>
      <th>'Feasible' Concepts Identified</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">Patients can't tell if they are doing the exercises correctly</td>
      <td>Camera and screen to track movement</td>
    </tr>
    <tr><td>Wearable sensors: EMG, gyroscope or accelerometer</td></tr>
    <tr><td>Device to limit bending angle or ROM (physical restraint)</td></tr>
    <tr><td>Recruit personal trainers or yoga instructors as trusted local sources of advice</td></tr>

   <tr>
      <td rowspan="2">Patients don't know if they are progressing</td>
      <td>Animated diagram visualising the actual surgical repair</td>
   </tr>
    <tr><td>Auto-generated weekly or monthly progress summaries based on recorded measurements</td></tr>

   <tr>
      <td rowspan="9">Patients struggle to find time and discipline to do the full set of prescribed exercises at home</td>
      <td>NTUC vouchers or rebates for achieving rehabilitation milestones</td>
    </tr>
    <tr><td>Online communities for sharing encouragement (e.g. Strava for rehabilitation)</td></tr>
    <tr><td>Asynchronous exercise sessions with rehabilitation buddies</td></tr>
    <tr><td>Personal rehabilitation avatar accompanying patients during exercises</td></tr>
    <tr><td>Incentives similar to Healthy 365 challenges</td></tr>
    <tr><td>Rehabilitation exercises converted into mini-games with progress levels and competition</td></tr>
    <tr><td>Portable device for shoulder rehabilitation</td></tr>
    <tr><td>Exercise-based alarm and desktop widget reminders</td></tr>
    <tr><td>Personalised rehabilitation avatar with progress updates</td></tr>

   <tr>
      <td rowspan="4">PT spending more time on reviewing notes and performing documentation</td>
      <td>Home rehabilitation sensors and patient scoring</td>
    </tr>
    <tr><td>Audio ambient scribe for automatic documentation of measurements and conversations</td></tr>
    <tr><td>AI-enabled prescriber that records session details, editable by PT</td></tr>
    <tr><td>Conversational AI patient intake providing structured summaries before appointments</td></tr>
  </tbody>
</table>


<table>
  <thead>
    <tr>
      <th>Problem(s)</th>
      <th>'Challenging' Concepts Identified</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Patients can't tell if they are doing the exercises correctly</td>
      <td>AI rehabilitation companion (e.g. Alexa or Google Home)</td>
    </tr>
    <tr><td>Pneumatic or hydraulic exoskeleton for controlled movement</td></tr>
    <tr><td>Auto-recorded PT sessions with a video library for patient reference</td></tr>

   <tr>
      <td>Patients don't know if they are progressing</td>
      <td>Telerehabilitation and remote evaluation combined with home-based sensor data</td>
    </tr>

   <tr>
      <td rowspan="3">Patients struggle to find time and discipline to do the full set of prescribed exercises at home</td>
      <td>Rehabilitation leaderboard for competition between patients</td>
   </tr>
    <tr><td>AI-suggested integration of rehabilitation exercises into everyday activities</td></tr>
    <tr><td>AI-based environment scanning to suggest rehabilitation exercises using nearby objects</td></tr>

   <tr>
      <td>PT spending more time on reviewing notes and performing documentation</td>
      <td>Multilingual conversation assessment and documentation</td>
    </tr>
  </tbody>
</table>

#### D.4 Concept(s) Evaluation

We initially came up with four concepts that addresses the identified barriers to different extents as shown below. The concepts had various features and methods to address the barriers we identified, ranging from phone-based application to wearable implementation.

| Concept Description | Supporting sketches |
|---|---|
| Digital Rehab Coach - An application that supports micro-rehab exercises that can be done anywhere and supports patients when transitioning from medical leave to working life. It also allows questions to be answered and steps to take to progress forward with their rehabilitation exercises. PTs can receive feedback from patients & provide input. | <img width="487" height="512" alt="image" src="https://github.com/user-attachments/assets/200a1da7-161c-4aa2-825b-a156ee395e8b" /> |
| Wearable supported micro-rehab tracking - A digital app guided with wearables that can measure ROM and encourage patients to sustain their exercises in form of ‘short-doses’ that can be done anywhere anytime. The app can track their progress and help set goals to achieve regularly, while providing a forum for patients to refer to for clarifications and sending a ‘time slip’ to PTs during sessions | <img width="512" height="290" alt="image" src="https://github.com/user-attachments/assets/fa93b55d-a79c-4b2c-a7ff-c40fe1ffde82" /> |
| Camera-based tracking - Digital capture of ROM via phone/electronic device while also providing a goal to achieve and tracking its progress, which PTs are able to view before each session. Brief feedback is provided in terms of rehabilitation progression shown in graphical format | <img width="512" height="469" alt="image" src="https://github.com/user-attachments/assets/762d8221-f175-4c74-a99b-c54325b84158" /> |
| A gamified application with a sensor wearable that encourages patients to do their exercises & win rewards by earning points, while providing feedback to them (on their form/reps). It also shows their progress over time while giving them checkpoints to assess their pain/tiredness levels. | <img width="350" height="512" alt="image" src="https://github.com/user-attachments/assets/f4a093e7-1f63-47a8-9e4c-934d08e788f9" /> |

However, we realised that these concepts agreed on 4 overlapping benefits: 1) Short exercises that adapt to settings, 2) Objective measurement, 3) Progress the patient can see, 4) Reviewed by physiotherapist. This made us reconsider the features to prioritise when developing our final solution at this initial stage, and whether they can meet the following criteria in the table shown below.

| The features our concepts proposed | Pain | Unmet | Feasible | What we did with it |
|---|---|---|---|---|
| An exercise regimen that fits the day | High | High | Medium | Lead feature. The only pain nobody on the market serves |
| A check on form and twisting | High | Medium | Medium | Already on the market. Our question is the trade-off between accuracy and the set-up burden we put on the patient |
| Objective range measurement | High | Low | High | Comes with the form check, and ROM measurement is the more mature, lower-complexity half of it |
| Answers between visits | High | Medium | Low | Technically hard. Fully personalised answers that are also accurate and safe would cost a great deal, so v1 keeps it light and limits the range of questions it answers |
| A report to the physiotherapist | Medium | Low | Medium | Out of scope for v1. Physiotherapists told us the need is weak and to be useful it would have to sit inside their workflow - meaning EHR integration, which is costly |
| Points, rewards, leaderboards | Medium | Low | High | The underlying motivation problem is not solved by rewards. Lower the barrier to doing it instead |

Thus, rather than separately developing the four concepts, we decided to converge the key benefits and features into one overarching solution that we decided to move forward with into the prototyping phase. This final solution mainly aims to provide necessary feedback and assistance patients need, aid them with progress tracking, and encourage them to adhere to their exercises by breaking them up and adjusting according to their schedule. The concepts of the final solution are shown below.

<img width="236" height="512" alt="image" src="https://github.com/user-attachments/assets/b792d2fe-599d-47bb-8464-0322759b95d6" /> <img width="236" height="512" alt="image" src="https://github.com/user-attachments/assets/fa5eae03-2987-4efa-9c2e-494612528277" /> <img width="236" height="512" alt="image" src="https://github.com/user-attachments/assets/ae8b8b9b-d7d7-492e-8100-cc5aaae6bde8" /> <img width="236" height="512" alt="image" src="https://github.com/user-attachments/assets/390a408d-5c45-4250-8ffe-a32059b93b41" /> <img width="236" height="512" alt="image" src="https://github.com/user-attachments/assets/a8981ecc-294c-48f3-b59c-7fcfeb9db459" /> <img width="512" height="228" alt="image" src="https://github.com/user-attachments/assets/444142ed-df6c-418f-a581-498cd98e59b9" />


[← Back to Section 2](#2-methodology--concept-development) | [↑ Back to contents](#table-of-contents)

### Appendix E: Test session findings

These tables set out what Participants A to I said and did. Quotes come from AI transcripts of the audio recordings and are lightly edited for clarity.

**How participants read each P1 screen**

| Participant | Screen 1 (behind) | Screen 2 (on track) | Screen 3 (ahead) | Said Screen 1 was behind? |
|---|---|---|---|---|
| A | "A bit lower" than the expected range (A, 00:44) | "Not bad... on track" (A, 01:42) | "Slightly better than on track?" (A, 01:03) | Yes |
| B | Improving, then "not so much" (B, 00:08) | "Constant improving" (B, 00:20) | Improvement slowed, then picked up (B, 00:25) | No |
| C | "Not recovering as well as expected", "still" distant from the goal (C, clip 1) | Recovering "well as expected", not far from the goal (C, clip 2) | "Much better than expected" (C, clip 3) | Yes |
| D | Improving, "a bit slower" from week 12 (D, 01:16) | Progress "very high" (D, 02:14) | "Back to normal by 14 weeks" (D, 02:14) | No |
| E | Line "stopping" (E, 00:09), "already outside" the range (E, 00:47) | "Within the range", "a good recovery" (E, 01:28) | "Very good", "you will recover faster" (E, 01:28) | Yes |
| F | No comment on individual screens. F called the tracker "intuitive" (F, 0:05) and said "I know where my progress is" (F, 0:11) | – | – | Not assessed |
| G | Against the expectation at 14 weeks, "not recovering good enough" (G, 00:14–00:37) | "Well within the expected range" (G, 00:37) | "Exceeding the expectation", "almost reached" the goal (G, 00:59) | Yes |
| H | In line with expectation up to week 10, then "not recovering well" (H, 00:28); about 60% confident of being on track (H, 01:31) | In line with the doctor's prescription (H, 02:04) | "Well ahead" of the required timeline (H, 02:21) | Yes |
| I | "Not reaching" the expected range, which "might discourage me" (I, clip 1, 00:01–00:34) | "Healing as expected" and "hitting the right target" (I, clip 1, 00:58) | "Doing better than I expected", felt "a bit superior" (I, clip 1, 00:58) | Yes |

**Key findings**

| Finding | What participants said or did | Design implication |
|---|---|---|
| Not all participants saw that the patient was behind | Of the 8 participants who commented on each screen, 6 compared Screen 1 with what was expected and said the patient was behind. B and D described only the line: B said improvement was "not so much" after a point (B, 00:08), and D saw "a progressive improvement" (D, 00:25), called weeks 12 to 14 "a bit slower" (D, 01:16) and was "positive" about the future (D, 01:39) | State plainly where the patient stands, and make being behind visible even when the line is rising (S2) |
| The chart did not tell participants what to do | F said: "if I'm performing below the expected range, what am I supposed to do?" (F, 0:11). On Screen 1, D would "increase my physiotherapy exercises" (D, 02:49), E thought "maybe exerting on my shoulder too much" (E, 00:47), and H would ask the doctor why recovery was not improving (H, 00:59). On Screen 3, E said they would not "need to go to rehabilitation or exercise too much" (E, 01:28). D wanted the screen to suggest what to do if progress is slow (D, 04:03). Participant I said being behind might discourage them because they were "still not sure why" (I, clip 1, 00:34), and on Screen 3 would ask the physiotherapist whether they were doing better than other patients (I, clip 1, 00:58) | Pair each status with a next step set by the physiotherapist, and make clear that being ahead does not end the programme (S2, S5) |
| Participants lacked guidance during exercise | A said: "I assume there'll be a camera here to check if you are doing it properly" (A, 02:12). During the repetitions, B asked: "What would you want me to do?" (B, 01:01) and "I don't understand what you want me to do" (B, 01:07), before working out that the arm should go up and down. The facilitator told A that the figure was "not really following you. You had to follow it" (A, 02:59). E thought the app was tracking the arm, like an Xbox 360, to see how high it was raised (E, 06:58). G counted along through both exercises and did not say they were unsure (G, 01:49–02:47). D said: "I may be pushing my arm in a wrong direction or a wrong angle", and wanted to see themselves and receive corrections (D, 08:43). D said the result should show accuracy: "if not, it doesn't mean anything" (D, 10:37). Participant I found the animations clear but "might feel a bit rushed" (I, clip 2, 00:44–00:58), said the pace was "determined by the video, not by me", and might move more slowly if in pain (I, clip 2, 01:34). Pausing was possible, but the animation "still doesn't really follow my own" movement (I, clip 2, 01:56) | Guide patients through each movement and wait for them to do it correctly, instead of counting automatically, and show how well they performed, not only how many repetitions they did (S1, S3) |
| Set-up was either slow or skipped | A took about 3 minutes to get into frame, from about 04:02 to 07:06, over the 2-minute target. A placed the phone on the floor (A, 04:25–05:12), noticed that the camera could zoom out (A, 06:02), and had a photo fall outside the lines (A, 06:23) before getting it right (A, 07:06). B did not set up the phone and went straight to the exercise, which ran whether or not the phone was in position (B, 00:35–00:55). D, E and H were asked to imagine that set-up was done (D, 05:06; E, 03:04; H, 05:23). Participant I had no live camera view and relied on the guide lines for the head and hips (I, clip 2, 00:23; 01:34) | Simplify phone placement, show a live preview, and check framing before the exercise starts (S3) |
| Pain shaped choices, but the score did not guide them | D would pick the exercise that hurt less (D, 06:28), would not push as hard on a painful prescribed exercise, and would tell the physiotherapist (D, 07:26). E said pain "is very subjective" and that it is best to try the exercise with the doctor first (E, 08:16–08:31). E was unsure whether a score meant recovery, overexertion or not having recovered yet (E, 09:13). H rated Exercise A 3 out of 10, wanted to try Exercise B to compare, and would choose exercises that cause less pain (H, 07:06–08:01). D would continue if pain was slight and stop if it was too much, and wanted the app to note where they paused (D, 09:41–09:51). E would stop when their body said so, and expected the app to ask about pain so they could report it to the doctor (E, 07:31–07:50). H would continue at levels up to 3 or 4, pause at 5 or 6, and stop if pain stayed high (H, 11:02–11:32), and wanted the app to say at which level to stop (H, 13:23). Participant I thought it was good that the app asked about pain (I, clip 2, 00:58) | Explain scores using a range set by the physiotherapist, state when to stop, and share pain and pauses with the physiotherapist (S4, S5) |

The following tables document the raw readings as captured from the 9 videos (3 videos each for 50°, 90°, 120°)
## Reference angle: 50° (Trial 1)

| clip | arm | reference_deg | trial | time_s | median_angle_deg | frames_in_bin |
| --- | --- | --- | --- | --- | --- | --- |
| right_050_1.mp4 | right | 50 | 1 | 0 | 5.214 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 0.1 | 4.699 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 0.2 | 4.431 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 0.3 | 4.409 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 0.4 | 3.64 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 0.5 | 3.714 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 0.6 | 4.17 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 0.7 | 4.727 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 0.8 | 5.17 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 0.9 | 5.479 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 1 | 6.605 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 1.1 | 6.929 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 1.2 | 6.921 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 1.3 | 7.076 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 1.4 | 7.344 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 1.5 | 9.16 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 1.6 | 11.304 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 1.7 | 13.946 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 1.8 | 18.854 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 1.9 | 21.508 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 2 | 25.296 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 2.1 | 26.634 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 2.2 | 28.916 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 2.3 | 31.268 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 2.4 | 33.98 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 2.5 | 37.179 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 2.6 | 38.761 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 2.7 | 40.668 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 2.8 | 42.181 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 2.9 | 45.13 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 3 | 47.833 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 3.1 | 49.764 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 3.2 | 51.586 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 3.3 | 52.914 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 3.4 | 52.732 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 3.5 | 52.446 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 3.6 | 52.05 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 3.7 | 51.7 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 3.8 | 51.751 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 3.9 | 51.819 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 4 | 51.746 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 4.1 | 51.103 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 4.2 | 50.353 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 4.3 | 50.421 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 4.4 | 50.606 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 4.5 | 50.748 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 4.6 | 50.651 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 4.7 | 50.747 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 4.8 | 50.368 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 4.9 | 49.5 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 5 | 48.49 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 5.1 | 46.649 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 5.2 | 44.758 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 5.3 | 40.387 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 5.4 | 37.11 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 5.5 | 31.857 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 5.6 | 28.995 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 5.7 | 23.874 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 5.8 | 22.391 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 5.9 | 18.702 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 6 | 14.302 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 6.1 | 9.748 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 6.2 | 7.489 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 6.3 | 6.098 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 6.4 | 5.228 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 6.5 | 5.682 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 6.6 | 5.506 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 6.7 | 5.689 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 6.8 | 6.019 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 6.9 | 6.15 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 7 | 5.89 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 7.1 | 5.917 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 7.2 | 6.15 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 7.3 | 5.506 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 7.4 | 5.491 | 3 |
| right_050_1.mp4 | right | 50 | 1 | 7.5 | 5.719 | 3 |

## Reference angle: 50° (Trial 2)

| clip | arm | reference_deg | trial | time_s | median_angle_deg | frames_in_bin |
| --- | --- | --- | --- | --- | --- | --- |
| right_050_2.mp4 | right | 50 | 2 | 0 | 6.001 | 4 |
| right_050_2.mp4 | right | 50 | 2 | 0.1 | 4.979 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 0.2 | 5.879 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 0.3 | 5.834 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 0.4 | 5.306 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 0.5 | 5.524 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 0.6 | 6.024 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 0.7 | 5.871 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 0.8 | 5.676 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 0.9 | 5.395 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 1 | 5.339 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 1.1 | 6.684 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 1.2 | 7.852 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 1.3 | 10.819 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 1.4 | 16.714 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 1.5 | 21.289 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 1.6 | 24.245 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 1.7 | 29.159 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 1.8 | 33.654 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 1.9 | 36.487 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 2 | 40.618 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 2.1 | 41.766 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 2.2 | 45.094 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 2.3 | 47.358 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 2.4 | 48.94 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 2.5 | 50.04 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 2.6 | 51.783 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 2.7 | 51.751 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 2.8 | 51.328 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 2.9 | 51.043 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 3 | 51.034 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 3.1 | 51.186 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 3.2 | 50.779 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 3.3 | 50.735 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 3.4 | 49.301 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 3.5 | 48.66 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 3.6 | 48.325 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 3.7 | 48.25 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 3.8 | 48.067 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 3.9 | 48.022 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 4 | 48.262 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 4.1 | 49.057 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 4.2 | 49.571 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 4.3 | 49.644 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 4.4 | 49.347 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 4.5 | 49.787 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 4.6 | 48.43 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 4.7 | 47.667 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 4.8 | 45.847 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 4.9 | 43.748 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 5 | 40.957 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 5.1 | 37.723 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 5.2 | 35.025 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 5.3 | 31.376 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 5.4 | 29.53 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 5.5 | 26.64 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 5.6 | 24.407 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 5.7 | 21.169 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 5.8 | 17.695 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 5.9 | 13.563 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 6 | 9.924 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 6.1 | 8.883 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 6.2 | 7.144 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 6.3 | 6.373 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 6.4 | 5.187 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 6.5 | 5.048 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 6.6 | 4.123 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 6.7 | 4.077 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 6.8 | 3.721 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 6.9 | 3.184 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 7 | 3.591 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 7.1 | 3.664 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 7.2 | 3.546 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 7.3 | 4.055 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 7.4 | 4.313 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 7.5 | 4.381 | 3 |
| right_050_2.mp4 | right | 50 | 2 | 7.6 | 4.454 | 2 |

## Reference angle: 50° (Trial 3)

| clip | arm | reference_deg | trial | time_s | median_angle_deg | frames_in_bin |
| --- | --- | --- | --- | --- | --- | --- |
| right_050_3.mp4 | right | 50 | 3 | 0 | 5.126 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 0.1 | 6.086 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 0.2 | 6.06 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 0.3 | 5.39 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 0.4 | 5.577 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 0.5 | 6.721 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 0.6 | 6.515 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 0.7 | 7.054 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 0.8 | 7.119 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 0.9 | 8.671 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 1 | 10.952 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 1.1 | 15.106 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 1.2 | 19.008 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 1.3 | 21.543 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 1.4 | 23.857 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 1.5 | 29.307 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 1.6 | 33.185 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 1.7 | 36.072 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 1.8 | 39.642 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 1.9 | 40.709 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 2 | 43.924 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 2.1 | 45.374 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 2.2 | 46.798 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 2.3 | 48.06 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 2.4 | 49.039 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 2.5 | 49.811 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 2.6 | 50.304 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 2.7 | 50.442 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 2.8 | 50.403 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 2.9 | 50.364 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 3 | 50.273 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 3.1 | 50.122 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 3.2 | 49.953 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 3.3 | 49.708 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 3.4 | 49.461 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 3.5 | 48.717 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 3.6 | 48.539 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 3.7 | 48.34 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 3.8 | 48.447 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 3.9 | 48.727 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 4 | 49.125 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 4.1 | 49.04 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 4.2 | 49.09 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 4.3 | 48.72 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 4.4 | 47.817 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 4.5 | 46.495 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 4.6 | 45.747 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 4.7 | 43.876 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 4.8 | 41.385 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 4.9 | 36.385 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 5 | 33.682 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 5.1 | 30.294 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 5.2 | 26.273 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 5.3 | 24.141 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 5.4 | 19.972 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 5.5 | 14.898 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 5.6 | 11.019 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 5.7 | 10.163 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 5.8 | 7.862 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 5.9 | 5.935 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 6 | 5.654 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 6.1 | 5.561 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 6.2 | 5.374 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 6.3 | 5.22 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 6.4 | 4.683 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 6.5 | 4.492 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 6.6 | 4.748 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 6.7 | 5.709 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 6.8 | 7.107 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 6.9 | 6.978 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 7 | 6.441 | 3 |
| right_050_3.mp4 | right | 50 | 3 | 7.1 | 6.406 | 3 |

## Reference angle: 90° (Trial 1)

| clip | arm | reference_deg | trial | time_s | median_angle_deg | frames_in_bin |
| --- | --- | --- | --- | --- | --- | --- |
| right_090_1.mp4 | right | 90 | 1 | 0 | 2.598 | 4 |
| right_090_1.mp4 | right | 90 | 1 | 0.1 | 3.772 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 0.2 | 4.765 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 0.3 | 4.055 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 0.4 | 4.455 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 0.5 | 4.47 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 0.6 | 3.496 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 0.7 | 0.692 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 0.8 | 0.73 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 0.9 | 0.765 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 1 | 1.079 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 1.1 | 6.318 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 1.2 | 14.747 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 1.3 | 17.988 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 1.4 | 29.504 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 1.5 | 35.997 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 1.6 | 42.742 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 1.7 | 46.375 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 1.8 | 56.223 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 1.9 | 66.497 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 2 | 70.572 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 2.1 | 76.836 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 2.2 | 79.492 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 2.3 | 77.285 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 2.4 | 78.018 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 2.5 | 81.473 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 2.6 | 83.235 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 2.7 | 84.94 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 2.8 | 85.332 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 2.9 | 86.983 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 3 | 87.98 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 3.1 | 88.791 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 3.2 | 88.964 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 3.3 | 88.105 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 3.4 | 88.118 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 3.5 | 87.809 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 3.6 | 86.928 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 3.7 | 87.13 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 3.8 | 87.101 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 3.9 | 87.028 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 4 | 87.119 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 4.1 | 86.996 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 4.2 | 87.203 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 4.3 | 88.18 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 4.4 | 86.405 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 4.5 | 80.642 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 4.6 | 77.465 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 4.7 | 71.959 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 4.8 | 65.918 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 4.9 | 58.52 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 5 | 49.618 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 5.1 | 42.852 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 5.2 | 36.004 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 5.3 | 29.033 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 5.4 | 22.399 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 5.5 | 15.84 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 5.6 | 8.793 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 5.7 | 1.736 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 5.8 | 0.15 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 5.9 | 0.313 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 6 | 0.647 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 6.1 | 0.286 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 6.2 | 0.78 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 6.3 | 2.928 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 6.4 | 2.833 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 6.5 | 2.254 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 6.6 | 2.33 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 6.7 | 3.257 | 3 |
| right_090_1.mp4 | right | 90 | 1 | 6.8 | 2.857 | 2 |

## Reference angle: 90° (Trial 2)

| clip | arm | reference_deg | trial | time_s | median_angle_deg | frames_in_bin |
| --- | --- | --- | --- | --- | --- | --- |
| right_090_2.mp4 | right | 90 | 2 | 0 | 1.978 | 4 |
| right_090_2.mp4 | right | 90 | 2 | 0.1 | 2.52 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 0.2 | 2.755 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 0.3 | 1.829 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 0.4 | 1.69 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 0.5 | 1.864 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 0.6 | 1.906 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 0.7 | 1.605 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 0.8 | 0.975 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 0.9 | 0.702 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 1 | 0.636 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 1.1 | 0.68 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 1.2 | 0.091 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 1.3 | 0.982 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 1.4 | 1.479 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 1.5 | 0.322 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 1.6 | 1.433 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 1.7 | 3.005 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 1.8 | 5.931 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 1.9 | 8.878 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 2 | 19.749 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 2.1 | 24.946 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 2.2 | 28.105 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 2.3 | 35.654 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 2.4 | 44.323 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 2.5 | 55.353 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 2.6 | 63.487 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 2.7 | 68.415 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 2.8 | 72.278 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 2.9 | 76.366 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 3 | 79.051 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 3.1 | 79.062 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 3.2 | 81.901 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 3.3 | 84.298 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 3.4 | 86.449 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 3.5 | 87.649 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 3.6 | 88.752 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 3.7 | 88.804 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 3.8 | 88.571 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 3.9 | 88.892 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 4 | 88.902 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 4.1 | 88.453 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 4.2 | 86.84 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 4.3 | 87.365 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 4.4 | 88.119 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 4.5 | 88.328 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 4.6 | 88.441 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 4.7 | 88.36 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 4.8 | 88.471 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 4.9 | 88.304 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 5 | 86.129 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 5.1 | 82.16 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 5.2 | 78.718 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 5.3 | 74.344 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 5.4 | 68.922 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 5.5 | 62.676 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 5.6 | 54.776 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 5.7 | 47.081 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 5.8 | 40.03 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 5.9 | 33.056 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 6 | 28.09 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 6.1 | 21.691 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 6.2 | 17.307 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 6.3 | 13.183 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 6.4 | 9.833 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 6.5 | 7.632 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 6.6 | 5.127 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 6.7 | 1.688 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 6.8 | 0.675 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 6.9 | 1.797 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 7 | 2.058 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 7.1 | 1.761 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 7.2 | 1.745 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 7.3 | 1.159 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 7.4 | 0.398 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 7.5 | 0.649 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 7.6 | 0.239 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 7.7 | 0.591 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 7.8 | 0.81 | 3 |
| right_090_2.mp4 | right | 90 | 2 | 7.9 | 0.413 | 2 |

## Reference angle: 90° (Trial 3)

| clip | arm | reference_deg | trial | time_s | median_angle_deg | frames_in_bin |
| --- | --- | --- | --- | --- | --- | --- |
| right_090_3.mp4 | right | 90 | 3 | 0 | 2.746 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 0.1 | 4.375 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 0.2 | 3.927 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 0.3 | 3.8 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 0.4 | 3.528 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 0.5 | 3.341 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 0.6 | 3.386 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 0.7 | 3.299 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 0.8 | 3.159 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 0.9 | 1.991 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 1 | 1.116 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 1.1 | 1.383 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 1.2 | 1.413 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 1.3 | 3.032 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 1.4 | 6.433 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 1.5 | 9.935 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 1.6 | 16.323 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 1.7 | 27.159 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 1.8 | 34.392 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 1.9 | 40.188 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 2 | 46.857 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 2.1 | 54.756 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 2.2 | 60.271 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 2.3 | 65.039 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 2.4 | 68.869 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 2.5 | 72.935 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 2.6 | 74.655 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 2.7 | 76.692 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 2.8 | 80.077 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 2.9 | 84.633 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 3 | 87.398 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 3.1 | 87.15 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 3.2 | 87.926 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 3.3 | 87.915 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 3.4 | 88.568 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 3.5 | 88.46 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 3.6 | 88.642 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 3.7 | 89.212 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 3.8 | 89.403 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 3.9 | 89.608 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 4 | 89.318 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 4.1 | 89.274 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 4.2 | 89.452 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 4.3 | 89.866 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 4.4 | 90.427 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 4.5 | 91.177 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 4.6 | 90.981 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 4.7 | 91.229 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 4.8 | 91.919 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 4.9 | 92.682 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 5 | 92.695 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 5.1 | 90.959 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 5.2 | 86.909 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 5.3 | 79.378 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 5.4 | 77.575 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 5.5 | 69.843 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 5.6 | 62.853 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 5.7 | 51.642 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 5.8 | 42.469 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 5.9 | 33.508 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 6 | 25.818 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 6.1 | 19.652 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 6.2 | 14.782 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 6.3 | 9.705 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 6.4 | 6.769 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 6.5 | 2.713 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 6.6 | 1.992 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 6.7 | 0.31 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 6.8 | 1.3 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 6.9 | 0.76 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 7 | 1.373 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 7.1 | 1.366 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 7.2 | 1.436 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 7.3 | 1.659 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 7.4 | 1.276 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 7.5 | 0.969 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 7.6 | 0.903 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 7.7 | 0.609 | 3 |
| right_090_3.mp4 | right | 90 | 3 | 7.8 | 0.769 | 3 |

## Reference angle: 120° (Trial 1)

| clip | arm | reference_deg | trial | time_s | median_angle_deg | frames_in_bin |
| --- | --- | --- | --- | --- | --- | --- |
| right_120_1.mp4 | right | 120 | 1 | 0 | 1.338 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 0.1 | 0.35 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 0.2 | 0.859 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 0.3 | 1.517 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 0.4 | 1.733 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 0.5 | 1.88 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 0.6 | 1.796 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 0.7 | 1.455 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 0.8 | 1.167 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 0.9 | 0.487 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 1 | 0.079 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 1.1 | 0.427 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 1.2 | 0.032 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 1.3 | 0.929 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 1.4 | 4.072 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 1.5 | 7.244 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 1.6 | 16.092 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 1.7 | 28.367 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 1.8 | 39.913 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 1.9 | 51.788 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 2 | 63.718 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 2.1 | 73.308 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 2.2 | 81.456 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 2.3 | 89.293 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 2.4 | 96.772 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 2.5 | 104.508 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 2.6 | 107.866 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 2.7 | 112.942 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 2.8 | 117.628 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 2.9 | 118.157 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 3 | 119.607 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 3.1 | 119.857 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 3.2 | 118.847 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 3.3 | 119.292 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 3.4 | 119.494 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 3.5 | 120.732 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 3.6 | 121.605 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 3.7 | 122.06 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 3.8 | 121.503 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 3.9 | 122.308 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 4 | 124.278 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 4.1 | 125.109 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 4.2 | 123.568 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 4.3 | 120.673 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 4.4 | 113.113 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 4.5 | 107.779 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 4.6 | 99.993 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 4.7 | 93.647 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 4.8 | 86.401 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 4.9 | 77.052 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 5 | 66.451 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 5.1 | 55.759 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 5.2 | 47.971 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 5.3 | 39.756 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 5.4 | 33.275 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 5.5 | 28.867 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 5.6 | 23.156 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 5.7 | 19.712 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 5.8 | 12.67 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 5.9 | 8.557 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 6 | 6.37 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 6.1 | 2.655 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 6.2 | 0.78 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 6.3 | 0.392 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 6.4 | 2.362 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 6.5 | 3.08 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 6.6 | 3.543 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 6.7 | 2.759 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 6.8 | 1.296 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 6.9 | 1.05 | 3 |
| right_120_1.mp4 | right | 120 | 1 | 7 | 1.452 | 3 |

## Reference angle: 120° (Trial 2)

| clip | arm | reference_deg | trial | time_s | median_angle_deg | frames_in_bin |
| --- | --- | --- | --- | --- | --- | --- |
| right_120_2.mp4 | right | 120 | 2 | 0 | 1.353 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 0.1 | 3.762 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 0.2 | 3.55 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 0.3 | 3.64 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 0.4 | 3.664 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 0.5 | 3.907 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 0.6 | 4.198 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 0.7 | 4.381 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 0.8 | 3.91 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 0.9 | 3.818 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 1 | 4.423 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 1.1 | 3.488 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 1.2 | 3.175 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 1.3 | 3.199 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 1.4 | 3.113 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 1.5 | 3.815 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 1.6 | 3.408 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 1.7 | 1.018 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 1.8 | 2.927 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 1.9 | 6.012 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 2 | 12.409 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 2.1 | 17.005 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 2.2 | 25.19 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 2.3 | 31.412 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 2.4 | 43.487 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 2.5 | 55.023 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 2.6 | 64.481 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 2.7 | 73.297 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 2.8 | 79.706 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 2.9 | 86.857 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 3 | 93.762 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 3.1 | 99.317 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 3.2 | 103.825 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 3.3 | 106.233 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 3.4 | 109.829 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 3.5 | 113.081 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 3.6 | 114.705 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 3.7 | 117.093 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 3.8 | 118.148 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 3.9 | 119.065 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 4 | 119.394 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 4.1 | 119.152 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 4.2 | 118.794 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 4.3 | 120 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 4.4 | 119.635 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 4.5 | 119.374 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 4.6 | 118.906 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 4.7 | 119.353 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 4.8 | 118.675 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 4.9 | 117.719 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 5 | 113.71 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 5.1 | 111.56 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 5.2 | 108.598 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 5.3 | 104.765 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 5.4 | 100.936 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 5.5 | 95.724 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 5.6 | 90.406 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 5.7 | 81.104 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 5.8 | 75.456 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 5.9 | 67.416 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 6 | 58.039 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 6.1 | 49.009 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 6.2 | 33.957 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 6.3 | 30.649 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 6.4 | 27.516 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 6.5 | 21.206 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 6.6 | 15.263 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 6.7 | 10.423 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 6.8 | 9.191 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 6.9 | 7.062 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 7 | 4.878 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 7.1 | 2.203 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 7.2 | 1.343 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 7.3 | 0.584 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 7.4 | 0.924 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 7.5 | 1.154 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 7.6 | 1.067 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 7.7 | 1.202 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 7.8 | 1.219 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 7.9 | 0.743 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 8 | 1.146 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 8.1 | 1.407 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 8.2 | 1.303 | 3 |
| right_120_2.mp4 | right | 120 | 2 | 8.3 | 1.539 | 2 |

## Reference angle: 120° (Trial 3)

| clip | arm | reference_deg | trial | time_s | median_angle_deg | frames_in_bin |
| --- | --- | --- | --- | --- | --- | --- |
| right_120_3.mp4 | right | 120 | 3 | 0 | 0.262 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 0.1 | 1.672 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 0.2 | 1.348 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 0.3 | 1.067 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 0.4 | 0.653 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 0.5 | 0.596 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 0.6 | 0.707 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 0.7 | 1.406 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 0.8 | 1.812 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 0.9 | 1.374 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 1 | 0.441 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 1.1 | 1.071 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 1.2 | 2.947 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 1.3 | 5.646 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 1.4 | 7.759 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 1.5 | 10.377 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 1.6 | 13.77 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 1.7 | 18.592 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 1.8 | 24.66 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 1.9 | 27.744 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 2 | 33.992 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 2.1 | 43.666 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 2.2 | 52.266 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 2.3 | 60.294 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 2.4 | 67.001 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 2.5 | 75.745 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 2.6 | 79.68 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 2.7 | 86.824 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 2.8 | 92.48 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 2.9 | 98.937 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 3 | 104.255 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 3.1 | 109.118 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 3.2 | 112.583 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 3.3 | 114.321 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 3.4 | 116.019 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 3.5 | 115.732 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 3.6 | 116.943 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 3.7 | 117.816 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 3.8 | 117.91 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 3.9 | 119.085 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 4 | 118.517 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 4.1 | 119.585 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 4.2 | 120.988 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 4.3 | 121.872 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 4.4 | 121.938 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 4.5 | 121.863 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 4.6 | 121.788 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 4.7 | 123.273 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 4.8 | 122.776 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 4.9 | 118.695 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 5 | 115.549 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 5.1 | 113.024 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 5.2 | 107.982 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 5.3 | 105.416 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 5.4 | 101.989 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 5.5 | 94.725 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 5.6 | 90.336 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 5.7 | 80.711 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 5.8 | 76.216 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 5.9 | 68.378 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 6 | 64.009 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 6.1 | 55.037 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 6.2 | 43.82 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 6.3 | 34.672 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 6.4 | 28.046 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 6.5 | 20.711 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 6.6 | 16.453 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 6.7 | 10.285 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 6.8 | 7.332 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 6.9 | 3.403 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 7 | 1.222 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 7.1 | 0.509 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 7.2 | 2.765 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 7.3 | 5.853 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 7.4 | 4.73 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 7.5 | 3.852 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 7.6 | 3.515 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 7.7 | 3.746 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 7.8 | 3.459 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 7.9 | 3.502 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 8 | 3.292 | 3 |
| right_120_3.mp4 | right | 120 | 3 | 8.1 | 3.381 | 2 |



[← Back to Section 5](#5-analysis) | [↑ Back to contents](#table-of-contents)

### Appendix F: Semester 2 prototypes

These prototypes need patients or clinicians, so they are planned for Semester 2. P1 and P2 will also be re-tested with patients.

| Design Question | Proposed Prototype | ID | Type | Spec |
|---|---|:---:|:---:|:---:|
| How useful do patients find the tracker and session flow, and why? | Patient re-test | P1, P2 | PoC | S2, S3 |
| How should feedback be given during an exercise, in terms of timing and visual, audio or haptic form? | Live feedback session | P4 | PoP | S1 |
| What kind of feedback do patients need, and how useful do they find it? | Live feedback session | P4 | PoC | S1 |
| How closely can camera or wearable tracking match a physiotherapist's rating of technique? | Technique detection and sensor mock-ups | P5 | PoP | S1 |
| What should a wearable sensor look like, and how do patients feel about wearing one? | Technique detection and sensor mock-ups | P5 | PoC | S1 |
| How can prescribed exercises be broken down into micro exercises that keep the prescribed dose? | Micro-rehab plan | P6 | PoP | S3 |
| How useful do patients find exercises adjusted to their schedules, and why? | Micro-rehab plan | P6 | PoC | S3 |
| How should a patient's question travel from being asked to receiving a trustworthy answer? | Question-answering service | P7 | PoP | S5 |
| How accurately can AI answer common post-RCR questions, and what combination of AI and clinician review keeps answers safe? | Question-answering service | P7 | PoP | S5 |
| Under what conditions would clinicians answer questions, and how does a forum compare with private messaging? | Question-answering service | P7 | PoC | S5 |
| What information do physiotherapists need, how long does a review take, and what do they do with it? | Physiotherapist summary | P8 | PoC | S4 |

**Note:** PoC - Proof of Concept, PoP - Proof of Principle

[← Back to Section 3](#3-fabrication-of-prototypes) | [↑ Back to contents](#table-of-contents)

