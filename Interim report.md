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

Recovery then follows a phased rehabilitation protocol lasting several months, progressing from sling immobilisation and passive range-of-motion exercises to active movement and strengthening (Sambandam, 2015). Most of this is done unsupervised at home, and adherence is low (Burns et al., 2021). Physiotherapists we interviewed estimated that 30–50% of patients do not do their home exercises and up to 20–30% drop out of public-sector physiotherapy, leading to prolonged recovery, residual stiffness and repeat care (Appendix B, B.5 and Theme 7). In Singapore's public hospitals, follow-ups are often 3–4 weeks apart, and capacity is unlikely to grow as care shifts towards the community (Ministry of Health, 2016; Appendix B, Theme 5).

Our interviews with 6 patients, 10 physiotherapists and 3 surgeons (Appendix B) and a survey of 6 patients (Appendix C) identified four barriers to adherence:

1. **Lack of time and discipline**, especially after patients return to work (7/10 physiotherapists; 3/6 survey respondents).
2. **Uncertainty about technique:** patients forget exercises or cannot tell whether their form is correct (8/10 physiotherapists).
3. **Misjudging progress:** patients often stop once they feel "good enough", around three months after surgery, before strength and range are restored (7/10 physiotherapists).
4. **Pain and fear of movement:** patients interpret pain as damage to the repair and stop exercising, leading to stiffness (7/10 physiotherapists; 2/6 survey respondents).

Of the 16 existing solutions we reviewed (Appendix A), digital exercise platforms such as Medbridge and Physitrack offer videos and reminders but no technique feedback. Sensor- and camera-based systems such as Rebee Health and Hinge Health give movement feedback, but mostly target general musculoskeletal care or the knee and report progress to clinicians. In Singapore, their uptake is further limited by data-protection rules and out-of-pocket costs (Appendix A.5). None describes showing patients their progress against the expected post-RCR trajectory, adapting exercises to daily routines, or giving RCR-specific guidance on pain. This project addresses these gaps.

### 1.3 Novelty and value proposition

For patients recovering from RCR who struggle to keep up their home exercises, ReMotion is a home rehabilitation solution that helps them exercise regularly, correctly and at a clinically appropriate pace. Built around the post-RCR recovery phases, it offers short sessions that fit into daily routines, feedback on technique, progress tracked against the expected recovery trajectory, and signals on acceptable pain and when to progress. There is early evidence that this approach works: a physiotherapist who shows patients their test results every session reported that it greatly improved adherence (Appendix B, Theme 3). ReMotion also gives physiotherapists a summary of progress between visits, saving consultation time. For the health system, better adherence could reduce stiffness-related delays and the number of patients referred back to physiotherapy (Appendix B, Theme 7). Each of these features exists separately in other products; ReMotion's novelty is combining them in one solution designed specifically for the home phase of recovery after RCR.

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
Considering our design specifications and taking the ACE framework as a guide, we ideated on the potential solutions we can develop to address them. The use of thinking tools such as ‘SCAMPER’ (Substitute, Combine, Adapt, Modify, Purpose, Eliminate, Reverse), ‘BruteThink’ and doing an ‘Idea Box’ enabled us to brainstorm ideas at the start. Afterwards, we review them against our Needs Criteria and organised them accordingly in the tables below.
> 

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






### 2.1 Chosen methodology / concept

[Content]

### 2.2 Evaluation against alternatives

> Evaluated in a systematic and comprehensive manner.

| Criterion (spec) | Weight | Concept A | Concept B | Concept C |
|---|---|---|---|---|
| [Criterion] (S1) | [w] | [Score] | [Score] | [Score] |
| [Criterion] (S2) | [w] | [Score] | [Score] | [Score] |
| **Weighted total** | | | | |

[Content]

## 3. Fabrication of Prototypes

> **~600 words.** What have you created to achieve the intended deliverables of your project? What are the purposes of these specimens or prototypes? How did you create these specimens or prototypes?

### 3.1 Detail design and low-fidelity prototype

> Multiple prototypes, thoughtfully created, with fine workmanship. Detail design, sketches and wireframes all count; state the purpose of each.

[Content]

### 3.2 How they were created

> Extensive references to and sound application of knowledge, principles and theories in relevant fields.

[Content]

## 4. Testing

> **~400 words.** What tests have you performed to investigate the key questions in your project? What are the purposes of these tests? How did you conduct these tests?

### 4.1 Purpose and scope of testing

> Clearly defined.

[Content]

### 4.2 Test approach

> Conducted conscientiously using the best possible approaches for the intended purposes. Walkthroughs of the low-fidelity prototype (3–5 participants, same task script) are suitable at the interim stage.

[Content]

## 5. Analysis

> **~650 words.** What have you found out through the specimens or prototypes which you have created and/or tests which you have conducted in your project? How do you know that your findings are valid?

### 5.1 Findings

> In-depth analysis and explanation of data and observations. Use the walkthrough observations and your needs research data.

| Finding | Evidence | Design implication |
|---|---|---|
| [Finding] | [Data / quotes / citation] | [Implication → spec] |

### 5.2 Methods and validity

> Precise use of appropriate methods, techniques, theories and/or concepts to explain key behaviour/trends.

[Content]

## 6. Discussion of Problems and Project Plan

> **~400 words.** What are the problems you faced or current shortcomings identified in your work? How do you plan to resolve them?

### 6.1 Problems faced and how they were resolved

> Detailed discussion.

[Content]

### 6.2 Shortcomings and proposed solutions

> Clearly identified, with sound and well-justified proposals.

[Content]

### 6.3 Project plan

> Detailed and viable, with well-articulated steps and clearly identified milestones.

| Milestone | Steps | Deliverable | Owner | Week |
|---|---|---|---|---|
| M1 | [Steps] | [Deliverable] | [Name] | [Week] |
| M2 | [Steps] | [Deliverable] | [Name] | [Week] |
| M3 | [Steps] | [Deliverable] | [Name] | [Week] |

## 7. Individual Contributions

> **~100 words.** Indicate individual areas of work clearly.

| Team member | Contribution |
|---|---|
| Raghavi | [Content] |
| Phyllis | [Content] |

## References

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
