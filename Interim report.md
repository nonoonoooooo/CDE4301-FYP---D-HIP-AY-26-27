# Rehabilitation Adherence After Rotator Cuff Repair

## CDE4301 Innovation & Design Capstone — Interim Report

**Project team:** Team Scapullama (Raghavi and Phyllis)  
**Semester:** Semester 1, AY2026/27  
**Supervisor(s):** Mark Chong Seow Khoon

> Word limit: 4,000 words excluding appendices. Delete all blockquotes before submission.

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

## 1. Objective, Scope and Context

### 1.1 Objective and scope

Recovery after rotator cuff repair (RCR) relies on months of home-based rehabilitation, yet patients receive little guidance or feedback between physiotherapy appointments. This project aims to design a home rehabilitation support system, ReMotion, that helps patients adhere to their prescribed programme after RCR, so that they progress safely towards clinically meaningful functional recovery by six months. 

- **In scope:** adults in Singapore in the home-based phase of rehabilitation after RCR, particularly working patients; fitting exercises into daily routines; feedback on exercise technique; tracking shoulder range of motion and strength against the expected recovery trajectory; guidance on acceptable pain and when to progress; and between-visit progress summaries for physiotherapists.
- **Out of scope:** replacing physiotherapists or changing surgical or rehabilitation protocols; diagnosing complications; non-surgical management of rotator cuff tears; and clinical effectiveness trials.

By the end of Semester 2, we aim to deliver a functional prototype evaluated with patients and physiotherapists against the specifications in Section 1.4. This is feasible because we have regular access to our clinical mentor, physiotherapists who have offered to help recruit participants, and industry fellows on our team with product development experience.

### 1.2 Context

Rotator cuff tears are among the most common causes of shoulder pain and disability (Simon et al., 2023), and their prevalence rises with age (Sripathi & Agrawal, 2024). When conservative management fails or the tear is large, patients may undergo surgical rotator cuff repair (RCR) (Sambandam, 2015).

Recovery then follows a phased rehabilitation protocol lasting several months, progressing from sling immobilisation and passive range-of-motion exercises to active movement and strengthening (Sambandam, 2015). Most of this is done unsupervised at home, and adherence is low (Burns et al., 2021). Physiotherapists we interviewed estimated that 30–50% of patients do not do their home exercises and up to 20–30% drop out of public-sector physiotherapy, leading to prolonged recovery, residual stiffness and repeat care (Appendix B, B.5 and Theme 7). In Singapore's public hospitals, follow-ups are often 3–4 weeks apart, which means there is a huge gap in between physiotherapy sessions where physiotherapists have no visibility into the patients' progress, and adherence depends on the patients' own discipline to carry out the prescribed physiotherapy exercises at home.

Our interviews with 6 patients, 10 physiotherapists and 3 surgeons (Appendix B) and a survey of 6 patients (Appendix C) identified four barriers to adherence:

1. **Lack of time and discipline**, especially after patients return to work (7/10 physiotherapists; 3/6 survey respondents).
2. **Uncertainty about technique:** patients forget exercises or cannot tell whether their form is correct (8/10 physiotherapists).
3. **Misjudging progress:** patients often stop once they feel "good enough", around three months after surgery, before strength and range are restored (7/10 physiotherapists).
4. **Pain and fear of movement:** patients interpret pain as damage to the repair and stop exercising, leading to stiffness (7/10 physiotherapists; 2/6 survey respondents).

Of the 16 existing solutions we reviewed (Appendix A), digital exercise platforms such as Medbridge and Physitrack offer videos and reminders but no technique feedback. Sensor- and camera-based systems such as Rebee Health and Hinge Health give movement feedback, but mostly target general musculoskeletal care or the knee and report progress to clinicians. In Singapore, their uptake is further limited by data-protection rules and out-of-pocket costs (Appendix A.5). None describes showing patients their progress against the expected post-RCR trajectory, adapting exercises to daily routines, or giving RCR-specific guidance on pain. This project addresses these gaps.

### 1.3 Novelty and value proposition

For patients recovering from RCR who struggle to keep up their home exercises, ReMotion is a home rehabilitation solution that helps them exercise regularly, correctly and at a clinically appropriate pace. Built around the post-RCR recovery phases, it offers short sessions that fit into daily routines, feedback on technique, progress tracked against the expected recovery trajectory, and signals on acceptable pain and when to progress. There is early evidence that this approach works: a physiotherapist who shows patients their test results every session reported that it greatly improved adherence (Appendix B, Theme 3). ReMotion also gives physiotherapists a summary of progress between visits, saving consultation time. For the health system, better adherence could reduce stiffness-related delays and the number of patients referred back to physiotherapy (Appendix B, Theme 7).

ReMotion's novelty lies in whom it is designed around. Most existing solutions are built for clinicians and the organisations that pay for care: their main buyers are clinicians, clinics, hospitals, employers and health plans (Appendix A.2), and their features serve clinical workflows, such as reducing administrative work (PhysioBuddy), integrating with medical records (Medbridge) and giving clinicians dashboards to monitor patients remotely (Appendix A.6). In these solutions, patient adherence is an expected benefit rather than the starting point of the design. ReMotion puts the patient's experience first: each feature is designed around a reason patients do not adhere, namely lack of time, uncertainty about technique, misjudging progress and fear of pain (Section 1.2). For example, ReMotion shows patients their own progress against the expected recovery trajectory, which none of the solutions we reviewed describes (Appendix A.6). Patient uptake of existing solutions also remains limited in Singapore: one sensor-based system has been taken up by 29 patients in a public hospital since March 2026, and printed exercise sheets and videos recorded on patients' phones remain the most common take-home materials (Appendix A.5).

### 1.4 Design specifications

| ID | Specification | Justification |
|---|---|---|
| S1 | The solution tells patients whether they are performing exercises correctly, agreeing with a physiotherapist's rating of the same repetitions at least 80% of the time. | Technique is checked only in session; 8/10 physiotherapists reported technique problems (Appendix B, Theme 2). |
| S2 | The solution shows patients how they are progressing, so that at least 4 of 5 test participants can correctly say whether they are on track. | Patients stop once they feel "good enough" (Appendix B, Theme 3); seeing progress was the most wanted support (5/6; Appendix C). |
| S3 | The solution fits into patients' schedules, taking no more time than their currently prescribed exercises, with set-up taking under 2 minutes. | Time was the most reported barrier; physiotherapists improve adherence by fitting exercises into routines (Appendix B, Theme 1; Appendix C). |
| S4 | The solution reduces the time physiotherapists spend reviewing patients' progress, with a between-visit summary they can review in under 2 minutes. | Physiotherapists see adherence only at the next visit and said a between-visit summary would save time (Appendix B, Theme 6). |
| S5 | The solution tells patients which pain is acceptable and when to progress, and never prompts movement beyond the range permitted for their rehabilitation phase. | Fear of pain was raised by 7/10 physiotherapists (Appendix B, Theme 4), and 4/6 survey respondents wanted to feel safe (Appendix C). |

## 2. Methodology / Concept Development

> **~700 words.** How do you intend to achieve the intended deliverables of your project? How do you know that your approach is suitable?
>
> Show the logic: barriers (why) → ideas → chosen direction (how). The prototype in Section 3 should follow naturally from this.
>
> Rubric A2 (Exceptional): chosen concept and its alternatives evaluated in a systematic and comprehensive manner.

### 2.1 Root Cause evaluation

 Barrier (Section 1.2) | Root cause | Design question | Spec |
|---|---|---|---|
| Lack of time and discipline | Work and daily commitments compete with rehabilitation. Patients may lose motivation once they feel sufficiently recovered and this may lead to low adoption rate. | How might we help patients incorporate prescribed rehabilitation exercises into their daily routines and sustain engagement throughout recovery | S3 |
| Uncertainty about technique | Patients receive limited feedback between PT appointments and PTs are only able to correct these exercises during sessions itself. | How might we enable patients to recognise and correct improper exercise techniques independently during home rehabilitation phase? | S1 |
| Misjudging progress | Patients have limited access to objective information on their progress unless requested and may mistake reduced pain or improved function for complete recovery. | How might we help patients understand their rehabilitation progress and potentially recognise when further improvement is needed? | S2 |
| Pain and fear of movement | Patients sometimes do not understand that the pain/discomfort during exercise is to be expected or whether the pain they feel requires them to seek professional advice | How might we help patients handle uncertainty about exercise-related pain and potentially continue rehabilitation safely within prescribed limits? | S5 |
| No visibility between visits | Home rehabilitation is largely self-managed, where PTs mostly rely on patient-reported responses and in-person reassessment.| How might we provide physiotherapists with relevant, actionable information about patients' home rehabilitation while minimising additional workload? | S4 |

### 2.2 Ideation

Following the identification of key rehabilitation barriers and establishment of design specifications and their justifications (Section 1), concept generation was conducted using ideation techniques, including SCAMPER, BruteThink and Idea Box. The resulting ideas were organised using the **Approach–Concept–Embodiment (ACE) framework**, progressing from broad solution strategies to specific concepts and potential implementations. Concepts were generated across the four main problem areas that were identified as barriers to rehabilitation. The main approaches are summarised in the table below, while the complete ACE framework is provided in Appendix D.1.

| Main Problem | Main Approaches explored |
|---|---|
| Uncertainty regarding exercise techniques | Movement tracking and feedback, Assisted movement, Self-guided learning |
| Difficulty assessing rehabilitation progress | Progress visualisation, Scoring System, Regular reviews |
| Limited time and discipline for doing rehabilitation exercises at home | Rewards and incentives, Social support, Gamification, Integration into daily routines |
| PTs spending more time on their administrative workload | Automated ROM documentation, Recorded note-taking of patients |

### 2.3 Concept selection

An initial screening was conducted to narrow the broad range of generated concepts according to their anticipated development and implementation feasibility. Concepts were classified as 'Easy', 'Feasible', 'Challenging' or 'Out of Scope'. 'Easy' concepts for instance demonstrate already established technology that simple to recreate, while 'Feasible' ones may require slight more resources or technology to develop but can be achieved. 'Challenging' concepts require vastly more resources or knowledge to validate and develop, while those under 'Out of scope' do not directly address the problems. The table below summarises the concepts that were categorised accordingly, with the complete screening results provided in Appendix D.2.

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
Scoring: 0 = Does not meet criterion; 1 = Meets criterion; 2 = Exceeds criterion. The thresholds are taken from your draft specifications, not established clinical standards.

Based on the needs-criteria evaluation, 'Feedback Provision' demonstrated the strongest alignment with our design specifications, particularly in providing exercise technique feedback and supporting safe rehabilitation. 'Rehabilitation Progress Tracking' was also identified as a promising complementary concept, allowing patients to better understand their recovery and providing relevant information for physiotherapists. Although 'Gamification' scored lower overall, it demonstrated potential in encouraging exercise adherence through integration into patients' daily routines. Therefore, feedback provision and progress tracking were prioritised for further development, with gamification considered as a supporting feature. These concepts will undergo initial prototyping to assess their technical feasibility and usability before further refinement.

## 3. Fabrication of Prototypes

> **~600 words.** What have you created to achieve the intended deliverables of your project? What are the purposes of these prototypes? How did you create them?
>
> Rubric A3 rates a section with nothing made as Poor ("prototypes could have been made, but not carried out"). This section is currently a plan: nothing below has been built yet. Once P1–P3 exist, change them to past tense, describe how they were made and add images.

### 3.1 Questions the prototypes will answer

We will not build one integrated prototype yet. Each prototype answers a small set of open questions at the lowest fidelity that can answer them, and any of them may be dropped or changed based on the results. The questions are of two types:

- **Proof of principle (PoP):** how the underlying mechanism works.
- **Proof of concept (PoC):** how the idea works for its users in practice, and what value they see in it.

At the interim stage we are testing without patients or physiotherapists, so we chose questions that do not depend on clinical judgement or on having had surgery: how easily a design is understood and used, and how a tracking method performs. Questions that need patients or clinicians move to Semester 2.

| ID | Prototype | Question | Type | Spec | Stage |
|---|---|---|---|---|---|
| P1 | Progress tracker | What should progress tracking look like so that first-time users can read it? | PoC | S2 | Interim |
| | | How do users interpret a chart showing someone who feels well but is behind the expected recovery? | PoC | S2 | |
| P2 | Exercise session flow | What steps make up one exercise session from start to finish? | PoC | S3 | Interim |
| | | How easy is each step for first-time users, and where do they struggle? | PoC | S3 | |
| P3 | Camera tracking test | How closely can a phone camera with pose estimation measure shoulder angle, compared with a manual reference? | PoP | S1 | Interim |
| | | How do camera position and arm angle affect the measurement? | PoP | S1 | |
| P1, P2 | Patient re-test | How useful do patients find the tracker and session flow, and why? | PoC | S2, S3 | Semester 2 |
| P4 | Live feedback session | How should feedback be given during an exercise, in terms of timing and visual, audio or haptic form? | PoP | S1 | Semester 2 |
| | | What kind of feedback do patients need, and how useful do they find it? | PoC | S1 | |
| P5 | Technique detection and sensor mock-ups | How closely can camera or wearable tracking match a physiotherapist's rating of technique? | PoP | S1 | Semester 2 |
| | | What should a wearable sensor look like, and how do patients feel about wearing one? | PoC | S1 | |
| P6 | Micro-rehab plan | How can prescribed exercises be broken down into micro exercises that keep the prescribed dose? | PoP | S3 | Semester 2 |
| | | How useful do patients find exercises adjusted to their schedules, and why? | PoC | S3 | |
| P7 | Question-answering service | How should a patient's question travel from being asked to receiving a trustworthy answer? | PoP | S5 | Semester 2 |
| | | How accurately can AI answer common post-RCR questions, and what combination of AI and clinician review keeps answers safe? | PoP | S5 | |
| | | Under what conditions would clinicians answer questions, and how does a forum compare with private messaging? | PoC | S5 | |
| P8 | Physiotherapist summary | What information do physiotherapists need, how long does a review take, and what do they do with it? | PoC | S4 | Semester 2 |

### 3.2 Prototypes for the interim stage

- **P1, progress tracker.** A one-screen mock-up, made in a design tool or slides, plotting a fictional patient's shoulder range of motion against an expected recovery band, linked to a personal goal such as reaching a high shelf. Three versions show a patient who is ahead, on track, and feeling well but behind. The third recreates the point around three months when patients stop (Appendix B, Theme 3). The recovery band is illustrative, not clinical data, because this test is about whether the chart can be read.
- **P2, exercise session flow.** A clickable mock-up of one session, from opening it to finishing: choosing the exercise, seeing instructions, doing the repetitions, reporting pain and viewing the result. The exercise shown is a placeholder.
- **P3, camera tracking test.** A phone video analysed with MediaPipe Pose, an open-source pose-estimation tool that locates body landmarks in video (Bazarevsky et al., 2020). A short script will calculate the shoulder angle from the shoulder, elbow and hip landmarks. Team members will raise an arm to reference angles marked with a protractor on a wall chart.

### 3.3 Prototypes for Semester 2

- **P4, live feedback session.** A team member will watch a participant exercise and give feedback by hand, using different forms and timings, in a Wizard-of-Oz set-up (Kelley, 1984). This shows what feedback helps before any detection system is built.
- **P5, technique detection and sensor mock-ups.** P3 measures angle only. P5 will extend it to judging technique, comparing the camera with wearable motion sensors (Appendix D) on an exercise chosen with a physiotherapist. Non-working foam or 3D-printed mock-ups will explore the sensor's shape and position.
- **P6, micro-rehab plan.** With physiotherapists, we will break prescribed exercises into short sessions, then link them to each participant's daily routines, because habits form through repeating a behaviour in a consistent context (Lally et al., 2010). The team will send reminders manually. Any breakdown will be approved by the participant's physiotherapist.
- **P7, question-answering service.** Common patient questions from our interviews, such as "I feel pain with this — is that normal?" (Appendix B, Theme 4), will be answered by an AI tool and by clinicians. A storyboard will show three ways to deliver answers: AI only, AI with clinician review, and a moderated forum. Timely answers aim to replace the fear-avoidance response of stopping at any pain (Vlaeyen & Linton, 2000). AI answers will be used for evaluation only and will not be given to patients as advice.
- **P8, physiotherapist summary.** A one-page document showing a fictional patient's exercise completion, range of motion against target, pain reports and flags, built around "compliance and whether they reach the target angle" (PT9).

The prototypes that prove useful will then be combined into the functional prototype for evaluation against S1–S5.

## 4. Testing

> **~400 words.** What tests have you performed to investigate the key questions in your project? What are the purposes of these tests? How did you conduct these tests?
>
> Rubric A4 rates a section with no testing done as Poor. No test has been run yet: this section is a plan. Run the P1–P3 tests, change Section 4.2 to past tense, and fill in the results and Section 5. Update the participant numbers to match what you actually did. Targets marked "proposed" are ours, not from the specifications; confirm them with your supervisor.

### 4.1 Purpose and scope

The interim tests check whether the tracker and session flow can be understood and used, and how well a phone camera measures shoulder angle. They use stand-in participants, so they cannot show that the designs are useful to patients, and they do not test clinical effectiveness or adherence, which are out of scope (Section 1.1). Results against S2 and S3 are therefore provisional until repeated with patients. P3 does not test S1 itself, which requires comparison with a physiotherapist's rating.

| ID | Method | Participants | What we record | Reference point |
|---|---|---|---|---|
| P1 | Task-based walkthrough | 5 stand-in participants | What participants say each version means and what they would do next | At least 4 of 5 correctly state whether the patient is on track (provisional; S2) |
| P2 | Task-based walkthrough | 5 stand-in participants | Steps completed unaided; where participants hesitate; time taken | Set-up under 2 minutes (provisional; S3) |
| P3 | Technical measurement | 2 team members | Difference between measured and reference angle, in degrees | Mean error within 10° (proposed) |

### 4.2 Interim tests: P1–P3

**P1 and P2.** Participants will be friends or family who have not seen the designs, including older adults where possible, because our survey respondents were aged 31–70 (Appendix C). Five participants per group suits this stage because a small group can reveal most usability problems in a design (Nielsen & Landauer, 1993). The results show how the designs work and why, not how common a response is.

Each session lasts about 15 minutes and follows the same script:

1. Introduce the scenario: imagine you are recovering from shoulder surgery and doing exercises at home. Explain that the design is being tested, not the participant, and that all data are fictional.
2. P1: show the three versions in random order. For each, ask where the patient stands and what they would do next.
3. P2: ask them to complete a session while thinking aloud, without help, and time it.
4. Close with what was confusing, missing or useful.

One team member will facilitate and the other will record answers, timings and quotes.

**P3.** Each team member will raise their arm to reference angles of 30°, 60°, 90°, 120° and 150°, repeated three times, filmed from the side and then from about 45°. We will calculate the mean error for each angle and camera position. Only team members will be filmed, and the movements are simple arm raises by uninjured people.

**Results:** [To complete after testing.]

### 4.3 Tests for Semester 2

- **P1 and P2:** repeat with patients, adding how useful they find the designs and why.
- **P4:** participants will do an exercise already prescribed to them while receiving feedback in different forms, then compare the forms.
- **P5:** we will film correct and deliberately incorrect repetitions from healthy participants, with physiotherapists rating each one independently of the system. Besides percentage agreement, we will report Cohen's kappa, which accounts for agreement by chance (Landis & Koch, 1977). Patients will wear the non-working mock-ups and describe how they feel.
- **P6:** a 1-week trial with 3–5 working patients, who will record daily whether they exercised, how long it took and why when they did not, with their current routine as the comparison.
- **P7:** clinicians will rate AI and clinician answers without knowing the source, then discuss what they would be willing to review. Patients will compare the three service models.
- **P8:** 5 physiotherapists will be timed from opening the summary until they state the patient's progress and their plan (under 2 minutes; S4).
- **Final evaluation:** the integrated functional prototype will be evaluated with patients and physiotherapists against all of S1–S5.

## 5. Analysis

> **~650 words.** What have you found out through the prototypes and tests, and how do you know your findings are valid?
>
> Rubric A5 (Exceptional): in-depth analysis through precise use of appropriate methods, techniques, theories and concepts to explain key behaviour and trends.

### 5.1 Findings

> In-depth analysis of the test results from Section 4.2, supported by the interview, survey and solution-review data (Appendices A–C). Explain the trends, not just list them, and state what each finding changes in the design.

| Finding | Evidence | Design implication |
|---|---|---|
| [Finding] | [Data / quotes / citation] | [Implication → spec] |

### 5.2 Methods and validity

> How the test and needs data were analysed (e.g. thematic analysis, counting how many participants raised each theme, triangulation across patients, physiotherapists, surgeons and the survey), and the limits of each, such as sample size and self-selection.

[Content]

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
| Raghavi | [Content] |
| Phyllis | [Content] |

## References

Bazarevsky, V., Grishchenko, I., Raveendran, K., Zhu, T., Zhang, F., & Grundmann, M. (2020). *BlazePose: On-device real-time body pose tracking*. arXiv. https://doi.org/10.48550/arXiv.2006.10204

Burns, D., Boyer, P., Razmjou, H., Richards, R., & Whyne, C. (2021). Adherence patterns and dose response of physiotherapy for rotator cuff pathology: Longitudinal cohort study. *JMIR Rehabilitation and Assistive Technologies, 8*(1), e21374. https://doi.org/10.2196/21374

Kelley, J. F. (1984). An iterative design methodology for user-friendly natural language office information applications. *ACM Transactions on Information Systems, 2*(1), 26–41. https://doi.org/10.1145/357417.357420

Lally, P., van Jaarsveld, C. H. M., Potts, H. W. W., & Wardle, J. (2010). How are habits formed: Modelling habit formation in the real world. *European Journal of Social Psychology, 40*(6), 998–1009. https://doi.org/10.1002/ejsp.674

Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics, 33*(1), 159–174. https://doi.org/10.2307/2529310

Nielsen, J., & Landauer, T. K. (1993). A mathematical model of the finding of usability problems. *Proceedings of the INTERACT '93 and CHI '93 Conference on Human Factors in Computing Systems*, 206–213. https://doi.org/10.1145/169059.169166

Sambandam, S. N. (2015). Rotator cuff tears: An evidence based approach. *World Journal of Orthopedics, 6*(11), 902. https://doi.org/10.5312/wjo.v6.i11.902

Simon, L. M., Nguyen, V., & Ezinwa, N. M. (2023). Acute shoulder injuries in adults. *American Family Physician, 107*(5), 503–512. https://www.aafp.org/afp/2023/0500/acute-shoulder-injuries

Sripathi, P., & Agrawal, D. K. (2024). Rotator cuff injury: Pathogenesis, biomechanics, and repair. *Journal of Orthopaedics and Sports Medicine, 6*(4). https://doi.org/10.26502/josm.511500167

Vlaeyen, J. W. S., & Linton, S. J. (2000). Fear-avoidance and its consequences in chronic musculoskeletal pain: A state of the art. *Pain, 85*(3), 317–332. https://doi.org/10.1016/S0304-3959(99)00242-0

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
      <td>Assess multi-lingual conversations</td>
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
