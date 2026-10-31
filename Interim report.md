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
7. [Individual Contributions](#7-individual-contributions)
8. [References](#references)
9. [Appendices](#appendices)
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

Recovery then follows a phased rehabilitation protocol lasting several months, progressing from sling immobilisation and passive range-of-motion exercises to active movement and strengthening (Sambandam, 2015). Most of this is done unsupervised at home, and adherence is low (Burns et al., 2021). Physiotherapists we interviewed estimated that 30–50% of patients do not do their home exercises and up to 20–30% drop out of public-sector physiotherapy, leading to prolonged recovery, residual stiffness and repeat care ([Appendix B, B.5](#b5-estimates-of-adherence-and-drop-off) and Theme 7). In Singapore's public hospitals, follow-ups are often 3–4 weeks apart, so physiotherapists cannot see patients' progress in between, and adherence depends on patients' own discipline.

Our interviews with 6 patients, 10 physiotherapists and 3 surgeons ([Appendix B](#appendix-b-summary-of-stakeholder-interviews)) and a survey of 6 patients ([Appendix C](#appendix-c-patient-survey)) identified four barriers to adherence:

1. **Lack of time and discipline**, especially after patients return to work (7/10 physiotherapists; 3/6 survey respondents).
2. **Uncertainty about technique:** patients forget exercises or cannot tell whether their form is correct (8/10 physiotherapists).
3. **Misjudging progress:** patients often stop once they feel "good enough", around three months after surgery, before strength and range are restored (7/10 physiotherapists).
4. **Pain and fear of movement:** patients interpret pain as damage to the repair and stop exercising, leading to stiffness (7/10 physiotherapists; 2/6 survey respondents).

Of the 16 existing solutions we reviewed ([Appendix A](#appendix-a-review-of-existing-solutions)), digital exercise platforms offer videos and reminders but no technique feedback, while sensor- and camera-based systems mostly target general musculoskeletal care or the knee. In Singapore, uptake is further limited by data-protection rules and out-of-pocket costs ([Appendix A.5](#a5-use-in-singapore-from-interviews)). None describes showing patients their progress against the expected post-RCR trajectory, adapting exercises to daily routines, or giving RCR-specific guidance on pain.

### 1.3 Novelty and value proposition

For patients recovering from RCR who struggle to keep up their home exercises, ReMotion is a home rehabilitation solution that helps them exercise regularly, correctly and at a clinically appropriate pace. Built around the post-RCR recovery phases, it offers short sessions that fit into daily routines, feedback on technique, and progress tracked against the expected recovery trajectory. There is early evidence that this approach works: a physiotherapist who shows patients their test results every session reported that it greatly improved adherence ([Appendix B, Theme 3](#b4-findings-by-theme)). ReMotion also gives physiotherapists a summary of progress between visits, saving consultation time. For the health system, better adherence could reduce stiffness-related delays and the number of patients referred back to physiotherapy ([Appendix B, Theme 7](#b4-findings-by-theme)).

ReMotion's novelty lies in whom it is designed around. Most existing solutions are built for clinicians and the organisations that pay for care: their main buyers are clinicians, clinics, hospitals, employers and health plans ([Appendix A.2](#a2-direct-competitors-profiles)), and their features serve clinical workflows, such as reducing administrative work (PhysioBuddy), integrating with medical records (Medbridge) and giving clinicians dashboards to monitor patients remotely ([Appendix A.6](#a6-gaps-against-our-specifications)). In these solutions, patient adherence is an expected benefit rather than the starting point of the design. ReMotion puts the patient's experience first: each feature is designed around a reason patients do not adhere, namely lack of time, uncertainty about technique, misjudging progress and fear of pain (Section 1.2). For example, ReMotion shows patients their own progress against the expected recovery trajectory, which none of the solutions we reviewed describes ([Appendix A.6](#a6-gaps-against-our-specifications)). Patient uptake of existing solutions also remains limited in Singapore, where printed sheets and phone videos are still the most common take-home materials ([Appendix A.5](#a5-use-in-singapore-from-interviews)).

### 1.4 Design specifications

| ID | Specification | Justification |
|---|---|---|
| S1 | The solution tells patients whether they are performing exercises correctly, agreeing with a physiotherapist's rating of the same repetitions at least 80% of the time. | Technique is checked only in session; 8/10 physiotherapists reported technique problems ([Appendix B, Theme 2](#b4-findings-by-theme)). |
| S2 | The solution shows patients how they are progressing, so that at least 4 of 5 test participants can correctly say whether they are on track. | Patients stop once they feel "good enough" ([Appendix B, Theme 3](#b4-findings-by-theme)); seeing progress was the most wanted support (5/6; [Appendix C](#appendix-c-patient-survey)). |
| S3 | The solution fits into patients' schedules, taking no more time than their currently prescribed exercises, with set-up taking under 2 minutes. | Time was the most reported barrier; physiotherapists improve adherence by fitting exercises into routines ([Appendix B, Theme 1](#b4-findings-by-theme); [Appendix C](#appendix-c-patient-survey)). |
| S4 | The solution reduces the time physiotherapists spend reviewing patients' progress, with a between-visit summary they can review in under 2 minutes. | Physiotherapists see adherence only at the next visit and said a between-visit summary would save time ([Appendix B, Theme 6](#b4-findings-by-theme)). |
| S5 | The solution tells patients which pain is acceptable and when to progress, and never prompts movement beyond the range permitted for their rehabilitation phase. | Fear of pain was raised by 7/10 physiotherapists ([Appendix B, Theme 4](#b4-findings-by-theme)), and 4/6 survey respondents wanted to feel safe ([Appendix C](#appendix-c-patient-survey)). |

## 2. Methodology / Concept Development

### 2.1 Root Cause evaluation

Barrier (Section 1.2) | Root cause | Design question | Spec |
|---|---|---|---|
| Lack of time and discipline | Work and daily commitments compete with rehabilitation. Patients may lose motivation once they feel sufficiently recovered and this may lead to low adoption rate. | How might we help patients incorporate prescribed rehabilitation exercises into their daily routines and sustain engagement throughout recovery? | S3 |
| Uncertainty about technique | Patients receive limited feedback between PT appointments and PTs are only able to correct these exercises during the sessions themselves. | How might we enable patients to recognise and correct improper exercise techniques independently during the home rehabilitation phase? | S1 |
| Misjudging progress | Patients have limited access to objective information on their progress unless requested and may mistake reduced pain or improved function for complete recovery. | How might we help patients understand their rehabilitation progress and potentially recognise when further improvement is needed? | S2 |
| Pain and fear of movement | Patients sometimes do not understand that the pain/discomfort during exercise is to be expected or whether the pain they feel requires them to seek professional advice | How might we help patients handle uncertainty about exercise-related pain and potentially continue rehabilitation safely within prescribed limits? | S5 |
| No visibility between visits | Home rehabilitation is largely self-managed, where PTs mostly rely on patient-reported responses and in-person reassessment.| How might we provide physiotherapists with relevant, actionable information about patients' home rehabilitation while minimising additional workload? | S4 |

### 2.2 Ideation

Following the identification of key rehabilitation barriers and establishment of design specifications and their justifications (Section 1), concept generation was conducted using ideation techniques, including SCAMPER, BruteThink and Idea Box. The resulting ideas were organised using the **Approach–Concept–Embodiment (ACE) framework**, progressing from broad solution strategies to specific concepts and potential implementations. Concepts were generated across the four main problem areas that were identified as barriers to rehabilitation. The main approaches are summarised in the table below, while the complete ACE framework is provided in [Appendix D.1](#d1-overall-ace-framework-for-concept-generation).

| Main Problem | Main Approaches explored |
|---|---|
| Uncertainty regarding exercise techniques | Movement tracking and feedback, Assisted movement, Self-guided learning |
| Difficulty assessing rehabilitation progress | Progress visualisation, Scoring System, Regular reviews |
| Limited time and discipline for doing rehabilitation exercises at home | Rewards and incentives, Social support, Gamification, Integration into daily routines |
| PTs spending more time on their administrative workload | Automated ROM documentation, Recorded note-taking of patients |

### 2.3 Concept selection

An initial screening was conducted to narrow the broad range of generated concepts according to their anticipated development and implementation feasibility. Concepts were classified as 'Easy', 'Feasible', 'Challenging' or 'Out of Scope'. 'Easy' concepts for instance demonstrate already established technology that is simple to recreate, while 'Feasible' ones may require slightly more resources or technology to develop but can be achieved. 'Challenging' concepts require vastly more resources or knowledge to validate and develop, while those under 'Out of scope' do not directly address the problems. The table below summarises the concepts that were categorised accordingly, with the complete screening results provided in [Appendix D.2](#d2-overall-concept-screening-categorisation).

| Screening category | Summarised concepts |
|---|---|
| Easy | Pre-recorded exercise videos, patient progress/evaluation graphs, goal setting and reminders, channel for feedback and support, micro-rehab exercises |
| Feasible | Camera-based movement tracking, wearable motion sensors, automated progress summaries, gamified incentives, AI-based prescriber (for PT) |
| Challenging | AI rehabilitation companion, robotic exoskeleton, AI-suggested exercises integrated into daily activities, group physiotherapy sessions, Tele-rehab, Auto-recorded PT sessions |
| Out of scope | Pain detection, Walk-in PT clinic, patient self-reflections, scanning device to track Range of Motion |

Following preliminary screening, three key concepts were shortlisted for further evaluation: Feedback Provision, Gamification (Incentivised Exercises), and Rehabilitation Progress Tracking. These concepts were prioritised as they directly address the major barriers identified through preliminary research, stakeholder interviews and observations of PT sessions. They also offer opportunities to support independent home rehabilitation without requiring continuous physiotherapist supervision. To assess their suitability, the shortlisted concepts were compared against the established design specifications (S1–S5) using a needs-criteria evaluation matrix as shown below.

| Design specification / Needs criteria | Feedback Provision | Gamification (Incentivised Exercises) | Rehabilitation Progress Tracking |
|---|:---:|:---:|:---:|
| Feedback on exercise technique (to see if they are doing it right) | 2 | 1 | 1 |
| Clear and understandable progress visibility for patients | 1 | 1 | 2 |
| Seamless integration into patients' schedule (no additional time needed) | 0 | 2 | 1 |
| Reduced PT time on (documentation) workload | 1 | 0 | 1 |
| Safe guidance (managing pain) | 2 | 0 | 0 |
| **Total score (maximum 10)** | **6** | **4** | **5** |

Scoring: 0 = Does not meet criterion; 1 = Meets criterion; 2 = Exceeds criterion. The thresholds are taken from our design specifications, not established clinical standards.

Based on the needs-criteria evaluation, 'Feedback Provision' demonstrated the strongest alignment with our design specifications, particularly in providing exercise technique feedback and supporting safe rehabilitation. 'Rehabilitation Progress Tracking' was also identified as a promising complementary concept, allowing patients to better understand their recovery and providing relevant information for physiotherapists. Although 'Gamification' scored lower overall, it demonstrated potential in encouraging exercise adherence through integration into patients' daily routines. Therefore, feedback provision and progress tracking were prioritised for further development, with gamification considered as a supporting feature. These concepts will undergo initial prototyping to assess their technical feasibility and usability before further refinement.

## 3. Fabrication of Prototypes

### 3.1 Questions the prototypes will answer

| ID | Prototype | Question | Type | Spec |
|---|---|---|---|---|
| P1 | Progress tracker | What should progress tracking look like so that first-time users can read it? | PoC | S2 |
| | | How do users interpret a chart showing someone who feels well but is behind the expected recovery? | PoC | S2 |
| P2 | Exercise session flow | What steps make up one exercise session from start to finish? | PoC | S3 |
| | | How easy is each step for first-time users, and where do they struggle? | PoC | S3 |
| P3 | Camera tracking test | How closely can a phone camera with pose estimation measure shoulder angle, compared with a manual reference? | PoP | S1 |
| | | How do camera position and arm angle affect the measurement? | PoP | S1 |

Prototypes that need patients or clinicians are planned for Semester 2 ([Appendix F](#appendix-f-semester-2-prototypes)).

### 3.2 Prototypes for the interim stage

The prototypes are in the [prototypes](prototypes) folder of this repository, and its [README](prototypes/README.md) explains how to run each one. We built them with AI assistance (Claude Code). P1 and P2 are self-contained web pages written in HTML, CSS and JavaScript, so they run in a phone browser and need no installation. We published them as web links for testing: [P1](https://claude.ai/artifact/6eKZh5YK9Trb4vgazCfDg2) and [P2](https://claude.ai/artifact/MCof3qxjA9kXrffwU7wZJs).

- **P1, progress tracker** ([source](prototypes/p1_progress_tracker/index.html)). A one-screen mock-up with a chart drawn in code, plotting a fictional patient's shoulder range of motion against an expected recovery band, linked to a personal goal such as reaching a high shelf. Three versions show a patient who is ahead, on track, and feeling well but behind. The third recreates the point around three months when patients stop ([Appendix B, Theme 3](#b4-findings-by-theme)). The versions are labelled only as Screens 1–3, so the labels do not give away the answer. The recovery band is illustrative, not clinical data, because this test is about whether the chart can be read.
- **P2, exercise session flow** ([source](prototypes/p2_session_flow/index.html)). A clickable mock-up of one session, from opening it to finishing: choosing the exercise, seeing instructions, setting up the phone, doing the repetitions, reporting pain and viewing the result. Two placeholder exercises use animated figures, one seen from the side and one from the front. Each cycle of the animation counts as one repetition. On the published link, the set-up screen uses a test photo to check framing, because the platform does not allow a live camera view. A facilitator panel on the last screen shows the time spent on each step.
- **P3, camera tracking test** ([source](prototypes/p3_camera_tracking/measure_angle.py)). A Python script that analyses phone video with MediaPipe Pose, an open-source pose-estimation tool that locates body landmarks in video (Bazarevsky et al., 2020). For each clip, it calculates the shoulder angle from the shoulder, elbow and hip landmarks, takes the median across frames to reduce the effect of wobble, and reports the mean error against the reference angle. Team members will raise an arm to reference angles marked with a protractor on a wall chart.

## 4. Testing

### 4.1 Purpose and scope

| ID | Method | Participants | What we record | Reference point |
|---|---|---|---|---|
| P1 | Task-based walkthrough | 2 stand-in participants (5 planned) | What participants say each version means and what they would do next | At least 4 of 5 correctly state whether the patient is on track (provisional; S2) |
| P2 | Task-based walkthrough | 2 stand-in participants (5 planned) | Steps completed unaided; where participants hesitate; time taken | Set-up under 2 minutes (provisional; S3) |
| P3 | Technical measurement | 2 team members | Difference between measured and reference angle, in degrees | Mean error within 10° (proposed) |

### 4.2 Interim tests: P1–P3

**P1 and P2.** We tested both prototypes with two family members as stand-in participants, in separate sessions of about 8 and 3 minutes, using a phone. We had planned five participants.

The sessions followed these steps:

1. **P1:** participants viewed the three screens and said what came to mind. Participant A was also asked how each patient was doing.
2. **P2:** participants worked through Exercise A and Exercise B.
3. **Set-up:** the published prototype could not show a live camera view, so Participant A used the test photo to check their position. Participant B did not set up the phone.

The facilitator stepped in when a participant needed help, for example to explain the high-shelf goal and the test photo. Both sessions were audio-recorded and transcribed ([Appendix E](#appendix-e-test-session-findings) summarises them).

**P3.** Each team member will raise their arm to reference angles of 30°, 60°, 90°, 120° and 150°, repeated three times, filmed from the side and then from about 45°. We will calculate the mean error for each angle and camera position. Only team members will be filmed, and the movements are simple arm raises by uninjured people.

## 5. Analysis

### 5.1 Findings

We tested P1 and P2 in two sessions with family members as stand-in participants, called Participants A and B. [Appendix E](#appendix-e-test-session-findings) sets out what each participant said and did. Three main findings emerged.

**Progress tracking (S2).** The chart could be read, but participants drew different conclusions from it: A compared patients with the expected range, while B followed the shape of the line. One likely reason is that the patient's line is the boldest element on the screen, while the expected range sits behind it as a pale band and nothing tells the reader what to conclude. A was also asked directly how each patient was doing, which may have prompted the comparison. B's unprompted reading mirrors how patients judge recovery ([Appendix B, Theme 3](#b4-findings-by-theme)), so a rising line could reassure a patient who is falling behind. The tracker should state plainly where the patient stands.

**Guidance during exercise (S1, S3).** Both participants appear to have assumed that the screen was following them, which left them unsure whether they were exercising correctly. This is an understandable assumption, because the set-up step asks users to position themselves in front of the phone, which implies that the phone will then watch them. Nothing on the exercise screen corrected this, and it began straight away, before they had time to work out their role. A more user-friendly design would guide patients through each movement and wait for them to do it correctly, instead of playing the exercise automatically and counting repetitions while they work out what to do.

**Set-up (S3).** Participants either struggled with set-up or skipped it: A took about 3 minutes, over the 2-minute target, and B did not set up the phone at all. The causes appear to differ. A had trouble trying to position the camera within the frame. B had no reason to set up, because the exercise ran whether or not the phone was in position, so set-up seemed optional. Together, these suggest that set-up must fit real home surroundings and must visibly matter to the session. This matches the positioning hassle reported with a previous system ([Appendix A.5](#a5-use-in-singapore-from-interviews)), and could add a new burden when time is already the most reported barrier ([Appendix B, Theme 1](#b4-findings-by-theme)). Prototype limitations such as the lack of a live camera view probably added to A's time, so this is a warning about framing, not a measure of a finished design. The design should simplify phone placement, show a live preview, and check framing before the exercise starts.

### 5.2 Methods and validity

The sessions were audio-recorded and transcribed by an AI tool. We grouped each participant's comments and actions by the questions in Section 3.1, compared the two sessions, and compared both with the interview and survey themes. Durations were estimated from recording timestamps, because the prototype's built-in timings were not read in Session 1.

These findings are early indications, not conclusions:

- **Sample:** we tested two participants, not the five planned, so each finding rests on one or two observations. The S2 target of 4 of 5 participants cannot be assessed.
- **Participants:** family members are not patients, and may respond more kindly than strangers. The sessions cannot show whether patients find either prototype useful.
- **Facilitation:** the facilitator sometimes explained features and gave positive feedback during tasks, which may have influenced later answers, and the two sessions were not run in exactly the same way.
- **Transcripts:** the AI transcripts are unclear in places, so we used only passages whose meaning was clear from context and lightly edited quotes for clarity.

## 6. Discussion of Problems and Project Plan

> **~400 words.** What are the problems you faced or current shortcomings identified in your work? How do you plan to resolve them?
>
> Rubric A6 (Exceptional): detailed discussion of how problems were resolved; major shortcomings clearly identified with sound, well-justified proposals; detailed, viable plan with well-articulated steps and clearly identified milestones.

### 6.1 Problems faced and how they were resolved

> Detailed discussion: each problem, what caused it, and what was done about it.

[Content]

### 6.2 Shortcomings and proposed solutions

> Clearly identified, with sound and well-justified proposals. Include the limits of the prototypes and tests so far (e.g. low fidelity, few participants, stand-in participants rather than patients or physiotherapists) and of the needs data (Appendices B.1, B.5 and C.5).

[Content]

### 6.3 Project plan

> Detailed and viable, with well-articulated steps and clearly identified milestones, from first prototype and test through to the Semester 2 evaluation against S1–S5.

| Milestone | Steps | Deliverable | Owner | Week |
|---|---|---|---|---|
| M1 | [Steps] | [Deliverable] | [Name] | [Week] |
| M2 | [Steps] | [Deliverable] | [Name] | [Week] |
| M3 | [Steps] | [Deliverable] | [Name] | [Week] |
| M4 | [Steps] | [Deliverable] | [Name] | [Week] |

## 7. Individual Contributions

> **~100 words.** Indicate individual areas of work clearly.

| Team member | Contribution |
|---|---|
| Raghavi | Wrote Section 2 and the P3 parts of Sections 4 and 5; built prototype P3 (camera tracking test) |
| Phyllis | Wrote Section 1 and the P1 and P2 parts of Sections 4 and 5; built prototypes P1 and P2 and ran their test sessions |

## References

Bazarevsky, V., Grishchenko, I., Raveendran, K., Zhu, T., Zhang, F., & Grundmann, M. (2020). *BlazePose: On-device real-time body pose tracking*. arXiv. https://doi.org/10.48550/arXiv.2006.10204

Burns, D., Boyer, P., Razmjou, H., Richards, R., & Whyne, C. (2021). Adherence patterns and dose response of physiotherapy for rotator cuff pathology: Longitudinal cohort study. *JMIR Rehabilitation and Assistive Technologies, 8*(1), e21374. https://doi.org/10.2196/21374

Sambandam, S. N. (2015). Rotator cuff tears: An evidence based approach. *World Journal of Orthopedics, 6*(11), 902. https://doi.org/10.5312/wjo.v6.i11.902

Simon, L. M., Nguyen, V., & Ezinwa, N. M. (2023). Acute shoulder injuries in adults. *American Family Physician, 107*(5), 503–512. https://www.aafp.org/afp/2023/0500/acute-shoulder-injuries

Sripathi, P., & Agrawal, D. K. (2024). Rotator cuff injury: Pathogenesis, biomechanics, and repair. *Journal of Orthopaedics and Sports Medicine, 6*(4). https://doi.org/10.26502/josm.511500167

## Appendices

### Appendix A: Review of existing solutions

#### A.1 Method

We identified 16 existing solutions through searches of company websites and published trials, supplemented by tools mentioned in our stakeholder interviews (Appendix B). We grouped them into direct competitors, which support home rehabilitation through software or sensors, and adjacent solutions, which are physical, robotic or VR equipment used mainly in specific phases or in clinics. Features were taken from each solution's official website or published trial. A dash (–) means the feature was not described in the information we reviewed, not that it is definitely absent.

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
| Feedback on technique (S1) | Sensor- and camera-based systems (Rebee Health, Kinexcs, Sword Health, Hinge Health, UINCARE Home+) | Digital exercise platforms give no technique feedback. Most sensor systems target general MSK care or the knee, and in Singapore their use is limited by out-of-pocket cost and set-up effort |
| Seeing progress (S2) | Most direct competitors track ROM or strength | Tracking is described mainly as clinician dashboards. None of the solutions reviewed describes showing patients their progress against the expected post-RCR trajectory |
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

#### D.1 Overall ACE Framework for concept generation

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
      <td rowspan="13"><b>(3) Patients struggle to find time and discipline to do the full set of prescribed exercises at home</b></td>
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
      <td rowspan="8"><b>APPROACH 2</b><br>Scoring system</td>
      <td rowspan="3"><b>Concept 2A</b><br>Competition</td>
      <td>Competing with other patients on the same recovery journey (e.g. Duolingo but for rehab) | Rehab Leaderboard</td>
    </tr>
    <tr><td>Competing as a group with patients from other groups (e.g. knee)</td></tr>
    <tr><td>Competing with family/friends who are trying to keep fit</td></tr>
    <tr>
      <td rowspan="5"><b>Concept 2B</b><br>Support group</td>
      <td>Group physiotherapy:<br>- At local community centres or zones, doing PT with fellow peers<br>- In groups with other patients (e.g. group-based PT session) with little PT supervision</td>
    </tr>
    <tr><td>Online communities to share encouragement (e.g. Strava for rehab)</td></tr>
    <tr><td>Asynchronous "exercise together" see when your buddy completes the same session</td></tr>
    <tr><td>Personal rehab avatar that accompanies patient during exercises, learning their habits and mood over time; shares progress updates with family/friends (with patient's approval), so loved ones can cheer them on without patient having to explain</td></tr>
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
      <td rowspan="13"><b>(3) Patients struggle to find time and discipline to do the full set of prescribed exercises at home</b></td>
      <td rowspan="5"><b>APPROACH 1</b><br>Gamification</td>
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
      <td rowspan="8"><b>APPROACH 2</b><br>Integration with daily routine</td>
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

#### D.2 Overall Concept screening categorisation

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

[← Back to Section 2](#2-methodology--concept-development) | [↑ Back to contents](#table-of-contents)

### Appendix E: Test session findings

This table sets out what Participants A and B said and did. Quotes come from AI transcripts of the audio recordings and are lightly edited for clarity. Times refer to each session's recording. Session 1 (Participant A) lasted about 8 minutes and Session 2 (Participant B) about 3 minutes.

| Finding | What participants said or did | Design implication |
|---|---|---|
| Participants read the chart in different ways | A identified the axes and said the patient was "progressively improving" (A, 00:25), then compared them with the expected range: "a bit lower" (A, 00:44). A read all three patients correctly, asking of the ahead patient "is it slightly better than on track?" (A, 01:03) and calling the on-track patient "not bad... on track" (A, 01:42). B described only the patient's own line, calling Screen 2 "constant improving" (B, 00:20) and saying that on Screen 3 improvement slowed for a while and then picked up again (B, 00:25) | State plainly where the patient stands against the expected range (S2) |
| The patient who was behind could still look like progress | B said this patient was improving, but that after a point the improvement was "not so much" (B, 00:08). B did not mention the patient being behind | Make being behind visible even when the line is rising (S2) |
| The exercise screen did not make clear what to do | A said: "I assume there'll be a camera here to check if you are doing it properly" (A, 02:12). During the repetitions, B asked: "What would you want me to do?" (B, 01:01) and "I don't understand what you want me to do" (B, 01:07), before working out that the arm should go up and down. The facilitator told A that the figure was "not really following you. You had to follow it" (A, 02:59) | Guide patients through each movement and wait for them to do it correctly, instead of counting automatically (S1, S3) |
| The test photo option was easily missed | The facilitator pointed out the camera function to A after Exercise A, and explained that the photo showed whether A was within the frame (A, 03:19) | Make framing a guided step (S3) |
| Set-up was either slow or skipped | A took about 3 minutes to get into frame, from about 04:02 to 07:06, over the 2-minute target. A placed the phone on the floor (A, 04:25–05:12), noticed that the camera could zoom out (A, 06:02), and had a photo fall outside the lines (A, 06:23) before getting it right (A, 07:06). B did not set up the phone and went straight to the exercise (B, 00:35–00:55) | Simplify phone placement, show a live preview, and check framing before the exercise starts (S3) |

[← Back to Section 5](#5-analysis) | [↑ Back to contents](#table-of-contents)

### Appendix F: Semester 2 prototypes

These prototypes need patients or clinicians, so they are planned for Semester 2. P1 and P2 will also be re-tested with patients.

| ID | Prototype | Question | Type | Spec |
|---|---|---|---|---|
| P1, P2 | Patient re-test | How useful do patients find the tracker and session flow, and why? | PoC | S2, S3 |
| P4 | Live feedback session | How should feedback be given during an exercise, in terms of timing and visual, audio or haptic form? | PoP | S1 |
| | | What kind of feedback do patients need, and how useful do they find it? | PoC | S1 |
| P5 | Technique detection and sensor mock-ups | How closely can camera or wearable tracking match a physiotherapist's rating of technique? | PoP | S1 |
| | | What should a wearable sensor look like, and how do patients feel about wearing one? | PoC | S1 |
| P6 | Micro-rehab plan | How can prescribed exercises be broken down into micro exercises that keep the prescribed dose? | PoP | S3 |
| | | How useful do patients find exercises adjusted to their schedules, and why? | PoC | S3 |
| P7 | Question-answering service | How should a patient's question travel from being asked to receiving a trustworthy answer? | PoP | S5 |
| | | How accurately can AI answer common post-RCR questions, and what combination of AI and clinician review keeps answers safe? | PoP | S5 |
| | | Under what conditions would clinicians answer questions, and how does a forum compare with private messaging? | PoC | S5 |
| P8 | Physiotherapist summary | What information do physiotherapists need, how long does a review take, and what do they do with it? | PoC | S4 |

[← Back to Section 3](#3-fabrication-of-prototypes) | [↑ Back to contents](#table-of-contents)
