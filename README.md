<h1 align="center">EMRA</h1>
<p align="center"><b>Educational Multimodal Robot Assistant</b></p>
<p align="center">A bilingual Arabic and English social robot for children with autism spectrum disorder.</p>

<p align="center">
  <img src="docs/interfaces/00-overview/00-main-menu-en.png" width="85%">
</p>

EMRA runs an activity suite on a touchscreen mounted on the robot's chest, with
an animated face on a circular head display. A conversational track listens to
the child, reads emotion from both speech and facial expression, and replies in
the language of the session. Ten activities cover conversation, body awareness,
visual matching, construction, colour, early numeracy, handwriting, shared
reading and letter work. An educator view reports progress per child and per
group, and generates written progress notes.

|  |  |
| --- | --- |
| Displays | 1080 x 1080 circular head, 1768 x 828 chest touchscreen |
| Languages | English and Arabic, with right to left layout |
| Robot side | Raspberry Pi 5 |
| Inference side | Workstation with an RTX 4080, English on port 8000, Arabic on port 8001 |

Every screen below is from the deployed system.

---

## Overview and session start

The chest touchscreen is the child's only point of contact with the system. It
opens on a menu of ten activities. An educator starts a session by entering the
child's name, age, identifier and gender, or continues as a guest when no
record is needed. Everything the child then does is logged against that
session, which is what the educator dashboard later reports on.

The activity set was shaped by the categories of application already in
routine use in autism therapy: communication and conversation practice,
body and self awareness, visual matching and construction, colour and shape
work, early numeracy, handwriting and tracing, shared reading, and letter and
phoneme work. EMRA covers those categories in one bilingual system running on
the robot rather than across separate tablet applications.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/00-overview/01-session-start-validation-en.png" width="100%"><br><sub>The session start panel rejects an empty form, so a child record or an explicit guest choice is always made before an activity opens.</sub></td>
<td width="50%"><img src="docs/interfaces/00-overview/02-session-start-filled-en.png" width="100%"><br><sub>Session start completed. Name, age, identifier and gender are bound to every record the session produces.</sub></td>
</tr>
</table>

## Talk with EMRA

Open conversation with EMRA. The child speaks, the robot listens, replies and
responds with a facial expression. This is the only activity that routes
through the language model. Speech is transcribed, emotion is read from both
the transcript and the child's face, the two channels are fused, and the fused
signal conditions the reply and the expression the robot shows. The
educational games are entirely separate from this track and never call the
language model.

_Screens for this activity are being captured._

## Body parts

Body Explorer teaches the child to identify facial parts and the hand in
English and Arabic. The child sits in front of the robot's camera and sees
themselves mirrored on the screen. Each round names one part, both as a
labelled illustration and as a spoken prompt, and the child answers by
pointing to that part on their own face.

Two computer vision models run on the live camera stream. A face landmark
model returns 468 three-dimensional facial landmarks per frame together with
expression signals, which fixes the on-screen position of the nose, eyes, ears
and mouth. A hand landmark model returns 21 hand landmarks, from which the
index fingertip is taken. On every frame the system measures the distance from
the fingertip to each candidate part and takes the nearest one. The answer
counts as correct only when the nearest part is the part that was requested
and the fingertip is held there for roughly half a second. When the fingertip
settles on a different part the round is rejected and the child is asked to try
again.

That nearest-part rule is what makes the activity discriminative rather than
merely motion sensitive: pointing at an eye when the mouth was named is
rejected. The teeth round adds the expression signals, so the child must point
at the mouth and show their teeth, which separates teeth from mouth despite the
shared location. The hand round only checks that a hand is visible. Hold times
and re-prompt thresholds are deliberately lenient to allow for imprecise motor
control at this age.

Spoken feedback is pre-rendered offline rather than synthesised at run time, so
the activity plays bilingual audio without loading a speech model. The module
is isolated from the rest of the robot software and cannot affect the
conversational track.

_Screens for this activity are being captured._

## Puzzle

Visual matching and spatial reasoning. Four pictures are offered across four
levels, with the piece count rising from two to six. The reference picture can
be shown on demand. Levels unlock in order, and a free play mode lets the child
replay anything already unlocked without the level gate.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/03-puzzle/01-level-select-en.png" width="100%"><br><sub>Level selection. Four levels, unlocked in order, with the piece count rising from two to six.</sub></td>
<td width="50%"><img src="docs/interfaces/03-puzzle/02-level-select-ar.png" width="100%"><br><sub>The same screen in Arabic. Layout, level order and progress state mirror to right to left.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/03-puzzle/03-gameplay-bus-en.png" width="100%"><br><sub>Level one, two pieces. The reference picture is available on demand from the bar above the board.</sub></td>
<td width="50%"><img src="docs/interfaces/03-puzzle/04-completion-bus-en.png" width="100%"><br><sub>Completion feedback. The solved picture is shown and the next level is unlocked.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/03-puzzle/06-gameplay-friends-en.png" width="100%"><br><sub>Level three, six pieces, with the unplaced pieces held in the tray below the board.</sub></td>
<td width="50%"><img src="docs/interfaces/03-puzzle/07-free-play-en.png" width="100%"><br><sub>Free play. Any unlocked picture can be replayed without the level gate.</sub></td>
</tr>
</table>

## LEGO build

Block construction against a target model. The target is displayed beside an
empty grid and the child drags bricks from the tray to reproduce it. Eight
models are available, ordered by the number of bricks and the number of
distinct colours involved.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/04-lego/01-level-select-en.png" width="100%"><br><sub>Level selection across eight target models, ordered by brick count and by the number of distinct colours.</sub></td>
<td width="50%"><img src="docs/interfaces/04-lego/02-gameplay-tree-en.png" width="100%"><br><sub>Building in progress. The target model sits at the top left, the working grid in the centre, and the available bricks in the tray below.</sub></td>
</tr>
</table>

## Painting

Colour by number. Each template pairs a line drawing with a numbered key, and
the child selects the crayon whose number matches the region. The reference
image stays visible for comparison. Seven templates run from five regions to
eight, so difficulty rises through both region count and region size.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/05-painting/01-rainbow-en.png" width="100%"><br><sub>Colour by number with five regions. The numbered key sits under the drawing and the reference image stays visible at the left.</sub></td>
<td width="50%"><img src="docs/interfaces/05-painting/05-elephant-en.png" width="100%"><br><sub>Six region template with clustered small regions, which raises the precision needed.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/05-painting/07-ice-cream-en.png" width="100%"><br><sub>Eight region template, the hardest in the set.</sub></td>
<td></td>
</tr>
</table>

## Colours

Two colour activities. The matching game asks the child to connect each named
crayon to its swatch, which tests colour naming rather than colour perception
alone. The discovery board presents eleven colour names, speaks each one, and
plays a short fill animation with the written word so the spoken name, the
written name and the colour are presented together.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/06-colors/01-menu-en.png" width="100%"><br><sub>Entry screen for the two colour activities.</sub></td>
<td width="50%"><img src="docs/interfaces/06-colors/02-match-gameplay-en.png" width="100%"><br><sub>Colour matching. Each named crayon is dragged to its swatch, so the task tests the colour name and not only the colour.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/06-colors/03-match-complete-en.png" width="100%"><br><sub>Feedback shown once every pair is matched.</sub></td>
<td width="50%"><img src="docs/interfaces/06-colors/04-discover-board-en.png" width="100%"><br><sub>Colour discovery board with eleven named colours, each spoken when selected.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/06-colors/05-reveal-animation-en.png" width="100%"><br><sub>Fill animation played after a colour is chosen.</sub></td>
<td width="50%"><img src="docs/interfaces/06-colors/06-word-reveal-en.png" width="100%"><br><sub>The written colour word shown with the spoken name, pairing the two forms.</sub></td>
</tr>
</table>

## Numbers

Early numeracy in two forms. Numeral tracing shows a dotted guide with a marked
starting point and speaks the number name as the stroke is completed. The
listening task speaks a number and asks the child to find it among floating
bubbles, which separates recognising the spoken word from producing the shape.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/07-numbers/00-menu-en.png" width="100%"><br><sub>Entry screen for the two number activities, tracing and the listening game.</sub></td>
<td width="50%"><img src="docs/interfaces/07-numbers/01-tracing-one-start-en.png" width="100%"><br><sub>Numeral tracing. The dotted guide carries a marked starting point and the number name is spoken as the stroke is made.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/07-numbers/02-tracing-one-success-en.png" width="100%"><br><sub>Completed trace with confirmation feedback.</sub></td>
<td width="50%"><img src="docs/interfaces/07-numbers/03-listen-find-one-en.png" width="100%"><br><sub>Listening task. A number is spoken and the matching bubble must be found, which separates hearing the word from writing the shape.</sub></td>
</tr>
</table>

## Writing

Handwriting and spelling. Word tracing shows a faded guide word inside the
writing area and fills each letter in colour as it is traced, in English and in
Arabic. The Arabic levels use connected letter forms with diacritics, so the
task is not a mirror of the English one. The spelling activity shows a picture
and asks the child to place letter tiles in order to build the word.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/08-writing/00-menu-en.png" width="100%"><br><sub>Entry screen for the two writing activities, word tracing and spelling.</sub></td>
<td width="50%"><img src="docs/interfaces/08-writing/01-tracing-level-select-en.png" width="100%"><br><sub>Word tracing level selection, three levels.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/08-writing/02-tracing-start-en.png" width="100%"><br><sub>Tracing task before the first stroke. The guide word sits faded inside the writing area.</sub></td>
<td width="50%"><img src="docs/interfaces/08-writing/03-tracing-progress-en.png" width="100%"><br><sub>Tracing in progress. Each letter fills with colour as it is completed.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/08-writing/04-tracing-success-en.png" width="100%"><br><sub>Success feedback with the pictured word, offering repetition or progression.</sub></td>
<td width="50%"><img src="docs/interfaces/08-writing/05-tracing-level-select-ar.png" width="100%"><br><sub>Arabic word tracing level selection.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/08-writing/06-tracing-progress-ar.png" width="100%"><br><sub>Arabic tracing in progress, using connected letter forms with diacritics rather than a transliteration of the English task.</sub></td>
<td width="50%"><img src="docs/interfaces/08-writing/07-spelling-level-select-en.png" width="100%"><br><sub>Spelling activity level selection, four levels.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/08-writing/08-spelling-gameplay-en.png" width="100%"><br><sub>Spelling. Letter tiles are placed in order to build the pictured word.</sub></td>
<td width="50%"><img src="docs/interfaces/08-writing/09-spelling-success-en.png" width="100%"><br><sub>Success feedback with the completed word.</sub></td>
</tr>
</table>

## Reading

Shared reading. Three short illustrated stories are narrated sentence by
sentence with the spoken word highlighted in the text, so the child follows the
written form while hearing it. Pages advance manually, which lets an educator
hold on a page for as long as the child needs.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/09-reading/01-contents-en.png" width="100%"><br><sub>Contents page listing three illustrated stories with their length.</sub></td>
<td width="50%"><img src="docs/interfaces/09-reading/02-story-star-en.png" width="100%"><br><sub>Story page during narration. The word being spoken is highlighted in the text.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/09-reading/03-story-seed-en.png" width="100%"><br><sub>Second story. Pages advance manually so an educator can hold on a page.</sub></td>
<td></td>
</tr>
</table>

## Letters

Letter work in two forms. In the recognition game the child picks a letter
tile from a row and a correct choice grows a flower and speaks an example word
beginning with that letter. Letter tracing then asks the child to produce the
shape, using the same dotted guide and start marker as the numeral task.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/10-letters/00-menu-en.png" width="100%"><br><sub>Entry screen for the two letter activities, the recognition garden and tracing.</sub></td>
<td width="50%"><img src="docs/interfaces/10-letters/01-flower-start-en.png" width="100%"><br><sub>Letter recognition. A letter is named and the child picks the matching tile from the row.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/10-letters/02-flower-letter-a-en.png" width="100%"><br><sub>Correct choice. The flower grows and an example word beginning with the letter is spoken.</sub></td>
<td width="50%"><img src="docs/interfaces/10-letters/04-tracing-a-start-en.png" width="100%"><br><sub>Letter tracing, using the same dotted guide and start marker as the numeral task.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/10-letters/05-tracing-a-success-en.png" width="100%"><br><sub>Completed trace with praise from the on-screen robot.</sub></td>
<td></td>
</tr>
</table>

## Educator dashboard

The educator view, reached from a separate entry point on the main menu. For a
single child it reports accuracy, mean response time, attempts, help usage,
level reached and stars earned, broken down by activity. For the whole
group it ranks children on the same measures. A report generator turns the
logged records into written progress notes covering strengths, difficulties and
suggested next steps, written in English or in Arabic depending on the language
chosen before the report is produced. Conversation sessions from the Talk
activity are listed separately with turn counts and duration, and a report can
be generated over selected sessions and e-mailed to the educator.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/01-children-list-en.png" width="100%"><br><sub>All enrolled children with per-activity progress, searchable by name or identifier.</sub></td>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/02-child-summary-en.png" width="100%"><br><sub>Single child summary. Accuracy, mean response time, attempts, help usage, level reached and stars, broken down by activity.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/03-visual-analysis-top-en.png" width="100%"><br><sub>Visual analysis. Headline counts and overall accuracy for one child.</sub></td>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/05-accuracy-by-subject-en.png" width="100%"><br><sub>Accuracy by activity.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/06-response-time-en.png" width="100%"><br><sub>Mean response time by activity, which exposes where a child is slow rather than inaccurate.</sub></td>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/07-stars-earned-en.png" width="100%"><br><sub>Stars earned by activity.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/08-class-overview-en.png" width="100%"><br><sub>Overview of the whole group. Number of children, mean accuracy, mean response time and total stars.</sub></td>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/09-accuracy-by-student-en.png" width="100%"><br><sub>Accuracy compared across all children in the group.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/10-students-table-en.png" width="100%"><br><sub>Full group table, sortable on age, stars, accuracy, mean time and activities attempted.</sub></td>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/12-llm-report-body-en.png" width="100%"><br><sub>Generated progress report covering strengths, difficulties and suggested next steps.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/14-talk-sessions-en.png" width="100%"><br><sub>Conversation sessions from the Talk activity, with turn count, duration and completion status.</sub></td>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/17-talk-report-body-en.png" width="100%"><br><sub>Generated conversation report covering engagement, language and emotion, and practical suggestions.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/18-talk-report-emailed-en.png" width="100%"><br><sub>Delivery confirmation for the report sent to the educator address.</sub></td>
<td></td>
</tr>
</table>

## Administrator panel

Maintenance functions behind an administrator sign in. The panel restores the
head servos to their neutral position on each rotation axis, which is needed
after transport or after a session in which the head was moved by hand.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/12-admin/01-login-en.png" width="100%"><br><sub>Administrator sign in, which keeps maintenance functions out of reach during a session.</sub></td>
<td width="50%"><img src="docs/interfaces/12-admin/02-panel-en.png" width="100%"><br><sub>Head servo calibration. Each rotation axis can be returned to its neutral position after transport or manual handling.</sub></td>
</tr>
</table>
