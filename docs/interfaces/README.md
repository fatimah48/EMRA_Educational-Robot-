# EMRA interface gallery

Screen captures of the deployed EMRA system, taken from the 1768x828
chest touchscreen. Sections follow the order the activities appear in on
the main menu. Each section opens with a description of what the
activity asks the child to do and how the response is judged, followed
by the captures for that activity in both languages.

Cite this gallery from the thesis by module and file name, for example
`03-puzzle/03-gameplay-bus-en.png`.

## Contents

- [Overview and session start](#00-overview) (2 figures)
- [Talk with EMRA](#01-talk) (pending capture)
- [Body parts](#02-body-parts) (pending capture)
- [Puzzle](#03-puzzle) (7 figures)
- [LEGO build](#04-lego) (2 figures)
- [Painting](#05-painting) (7 figures)
- [Colours](#06-colors) (6 figures)
- [Numbers](#07-numbers) (5 figures)
- [Writing](#08-writing) (9 figures)
- [Reading](#09-reading) (4 figures)
- [Letters](#10-letters) (5 figures)
- [Educator dashboard](#11-educator-dashboard) (pending capture)
- [Administrator panel](#12-admin) (2 figures)

<a id="00-overview"></a>

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

**`00-overview/00-main-menu-en.png`** Main menu. Ten activities, the educator entry point at the left, and the session start panel at the right.

<img src="00-overview/00-main-menu-en.png" width="700">

**`00-overview/01-session-start-validation-en.png`** The session start panel rejects an empty form, so a child record or an explicit guest choice is always made before an activity opens.

<img src="00-overview/01-session-start-validation-en.png" width="700">

<a id="01-talk"></a>

## Talk with EMRA

Open conversation with EMRA. The child speaks, the robot listens, replies and
responds with a facial expression. This is the only activity that routes
through the language model. Speech is transcribed, emotion is read from both
the transcript and the child's face, the two channels are fused, and the fused
signal conditions the reply and the expression the robot shows. The
educational games are entirely separate from this track and never call the
language model.

_Captures pending._

<a id="02-body-parts"></a>

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

_Captures pending._

<a id="03-puzzle"></a>

## Puzzle

Visual matching and spatial reasoning. Four pictures are offered across four
levels, with the piece count rising from two to six. The reference picture can
be shown on demand. Levels unlock in order, and a free play mode lets the child
replay anything already unlocked without the level gate.

**`03-puzzle/01-level-select-en.png`** Level selection. Four levels, unlocked in order, with the piece count rising from two to six.

<img src="03-puzzle/01-level-select-en.png" width="700">

**`03-puzzle/02-level-select-ar.png`** The same screen in Arabic. Layout, level order and progress state mirror to right to left.

<img src="03-puzzle/02-level-select-ar.png" width="700">

**`03-puzzle/03-gameplay-bus-en.png`** Level one, two pieces. The reference picture is available on demand from the bar above the board.

<img src="03-puzzle/03-gameplay-bus-en.png" width="700">

**`03-puzzle/04-completion-bus-en.png`** Completion feedback. The solved picture is shown and the next level is unlocked.

<img src="03-puzzle/04-completion-bus-en.png" width="700">

**`03-puzzle/05-gameplay-flower-en.png`** Level two, four pieces.

<img src="03-puzzle/05-gameplay-flower-en.png" width="700">

**`03-puzzle/06-gameplay-friends-en.png`** Level three, six pieces, with the unplaced pieces held in the tray below the board.

<img src="03-puzzle/06-gameplay-friends-en.png" width="700">

**`03-puzzle/07-free-play-en.png`** Free play. Any unlocked picture can be replayed without the level gate.

<img src="03-puzzle/07-free-play-en.png" width="700">

<a id="04-lego"></a>

## LEGO build

Block construction against a target model. The target is displayed beside an
empty grid and the child drags bricks from the tray to reproduce it. Eight
models are available, ordered by the number of bricks and the number of
distinct colours involved.

**`04-lego/01-level-select-en.png`** Level selection across eight target models, ordered by brick count and by the number of distinct colours.

<img src="04-lego/01-level-select-en.png" width="700">

**`04-lego/02-gameplay-tree-en.png`** Building in progress. The target model sits at the top left, the working grid in the centre, and the available bricks in the tray below.

<img src="04-lego/02-gameplay-tree-en.png" width="700">

<a id="05-painting"></a>

## Painting

Colour by number. Each template pairs a line drawing with a numbered key, and
the child selects the crayon whose number matches the region. The reference
image stays visible for comparison. Seven templates run from five regions to
eight, so difficulty rises through both region count and region size.

**`05-painting/01-rainbow-en.png`** Colour by number with five regions. The numbered key sits under the drawing and the reference image stays visible at the left.

<img src="05-painting/01-rainbow-en.png" width="700">

**`05-painting/02-number-six-en.png`** Template combining numeral recognition with colour matching.

<img src="05-painting/02-number-six-en.png" width="700">

**`05-painting/03-duck-en.png`** Five region template.

<img src="05-painting/03-duck-en.png" width="700">

**`05-painting/04-turtle-en.png`** Six region template.

<img src="05-painting/04-turtle-en.png" width="700">

**`05-painting/05-elephant-en.png`** Six region template with clustered small regions, which raises the precision needed.

<img src="05-painting/05-elephant-en.png" width="700">

**`05-painting/06-house-en.png`** Five region template.

<img src="05-painting/06-house-en.png" width="700">

**`05-painting/07-ice-cream-en.png`** Eight region template, the hardest in the set.

<img src="05-painting/07-ice-cream-en.png" width="700">

<a id="06-colors"></a>

## Colours

Two colour activities. The matching game asks the child to connect each named
crayon to its swatch, which tests colour naming rather than colour perception
alone. The discovery board presents eleven colour names, speaks each one, and
plays a short fill animation with the written word so the spoken name, the
written name and the colour are presented together.

**`06-colors/01-menu-en.png`** Entry screen for the two colour activities.

<img src="06-colors/01-menu-en.png" width="700">

**`06-colors/02-match-gameplay-en.png`** Colour matching. Each named crayon is dragged to its swatch, so the task tests the colour name and not only the colour.

<img src="06-colors/02-match-gameplay-en.png" width="700">

**`06-colors/03-match-complete-en.png`** Feedback shown once every pair is matched.

<img src="06-colors/03-match-complete-en.png" width="700">

**`06-colors/04-discover-board-en.png`** Colour discovery board with eleven named colours, each spoken when selected.

<img src="06-colors/04-discover-board-en.png" width="700">

**`06-colors/05-reveal-animation-en.png`** Fill animation played after a colour is chosen.

<img src="06-colors/05-reveal-animation-en.png" width="700">

**`06-colors/06-word-reveal-en.png`** The written colour word shown with the spoken name, pairing the two forms.

<img src="06-colors/06-word-reveal-en.png" width="700">

<a id="07-numbers"></a>

## Numbers

Early numeracy in two forms. Numeral tracing shows a dotted guide with a marked
starting point and speaks the number name as the stroke is completed. The
listening task speaks a number and asks the child to find it among floating
bubbles, which separates recognising the spoken word from producing the shape.

**`07-numbers/01-tracing-one-start-en.png`** Numeral tracing. The dotted guide carries a marked starting point and the number name is spoken as the stroke is made.

<img src="07-numbers/01-tracing-one-start-en.png" width="700">

**`07-numbers/02-tracing-one-success-en.png`** Completed trace with confirmation feedback.

<img src="07-numbers/02-tracing-one-success-en.png" width="700">

**`07-numbers/03-listen-find-one-en.png`** Listening task. A number is spoken and the matching bubble must be found, which separates hearing the word from writing the shape.

<img src="07-numbers/03-listen-find-one-en.png" width="700">

**`07-numbers/04-listen-find-four-en.png`** Listening task with correct answer feedback delivered by the on-screen robot.

<img src="07-numbers/04-listen-find-four-en.png" width="700">

**`07-numbers/05-listen-find-six-en.png`** Final item of level one.

<img src="07-numbers/05-listen-find-six-en.png" width="700">

<a id="08-writing"></a>

## Writing

Handwriting and spelling. Word tracing shows a faded guide word inside the
writing area and fills each letter in colour as it is traced, in English and in
Arabic. The Arabic levels use connected letter forms with diacritics, so the
task is not a mirror of the English one. The spelling activity shows a picture
and asks the child to place letter tiles in order to build the word.

**`08-writing/01-tracing-level-select-en.png`** Word tracing level selection, three levels.

<img src="08-writing/01-tracing-level-select-en.png" width="700">

**`08-writing/02-tracing-start-en.png`** Tracing task before the first stroke. The guide word sits faded inside the writing area.

<img src="08-writing/02-tracing-start-en.png" width="700">

**`08-writing/03-tracing-progress-en.png`** Tracing in progress. Each letter fills with colour as it is completed.

<img src="08-writing/03-tracing-progress-en.png" width="700">

**`08-writing/04-tracing-success-en.png`** Success feedback with the pictured word, offering repetition or progression.

<img src="08-writing/04-tracing-success-en.png" width="700">

**`08-writing/05-tracing-level-select-ar.png`** Arabic word tracing level selection.

<img src="08-writing/05-tracing-level-select-ar.png" width="700">

**`08-writing/06-tracing-progress-ar.png`** Arabic tracing in progress, using connected letter forms with diacritics rather than a transliteration of the English task.

<img src="08-writing/06-tracing-progress-ar.png" width="700">

**`08-writing/07-spelling-level-select-en.png`** Spelling activity level selection, four levels.

<img src="08-writing/07-spelling-level-select-en.png" width="700">

**`08-writing/08-spelling-gameplay-en.png`** Spelling. Letter tiles are placed in order to build the pictured word.

<img src="08-writing/08-spelling-gameplay-en.png" width="700">

**`08-writing/09-spelling-success-en.png`** Success feedback with the completed word.

<img src="08-writing/09-spelling-success-en.png" width="700">

<a id="09-reading"></a>

## Reading

Shared reading. Three short illustrated stories are narrated sentence by
sentence with the spoken word highlighted in the text, so the child follows the
written form while hearing it. Pages advance manually, which lets an educator
hold on a page for as long as the child needs.

**`09-reading/01-contents-en.png`** Contents page listing three illustrated stories with their length.

<img src="09-reading/01-contents-en.png" width="700">

**`09-reading/02-story-star-en.png`** Story page during narration. The word being spoken is highlighted in the text.

<img src="09-reading/02-story-star-en.png" width="700">

**`09-reading/03-story-seed-en.png`** Second story. Pages advance manually so an educator can hold on a page.

<img src="09-reading/03-story-seed-en.png" width="700">

**`09-reading/04-story-cat-en.png`** Third story.

<img src="09-reading/04-story-cat-en.png" width="700">

<a id="10-letters"></a>

## Letters

Letter work in two forms. In the recognition game the child picks a letter
tile from a row and a correct choice grows a flower and speaks an example word
beginning with that letter. Letter tracing then asks the child to produce the
shape, using the same dotted guide and start marker as the numeral task.

**`10-letters/01-flower-start-en.png`** Letter recognition. A letter is named and the child picks the matching tile from the row.

<img src="10-letters/01-flower-start-en.png" width="700">

**`10-letters/02-flower-letter-a-en.png`** Correct choice. The flower grows and an example word beginning with the letter is spoken.

<img src="10-letters/02-flower-letter-a-en.png" width="700">

**`10-letters/03-flower-letter-b-en.png`** A later item in the same level.

<img src="10-letters/03-flower-letter-b-en.png" width="700">

**`10-letters/04-tracing-a-start-en.png`** Letter tracing, using the same dotted guide and start marker as the numeral task.

<img src="10-letters/04-tracing-a-start-en.png" width="700">

**`10-letters/05-tracing-a-success-en.png`** Completed trace with praise from the on-screen robot.

<img src="10-letters/05-tracing-a-success-en.png" width="700">

<a id="11-educator-dashboard"></a>

## Educator dashboard

The educator view, reached from a separate entry point on the main menu. For a
single child it reports accuracy, mean response time, attempts, help usage,
level reached and stars earned, broken down by activity. For the cohort it
ranks children on the same measures. A report generator turns the logged
records into written progress notes in English or Arabic covering strengths,
difficulties and suggested next steps. Conversation sessions from the Talk
activity are listed separately with turn counts and duration, and a report can
be generated over selected sessions and e-mailed to the educator.

_Captures pending._

<a id="12-admin"></a>

## Administrator panel

Maintenance functions behind an administrator sign in. The panel restores the
head servos to their neutral position on each rotation axis, which is needed
after transport or after a session in which the head was moved by hand.

**`12-admin/01-login-en.png`** Administrator sign in, which keeps maintenance functions out of reach during a session.

<img src="12-admin/01-login-en.png" width="700">

**`12-admin/02-panel-en.png`** Head servo calibration. Each rotation axis can be returned to its neutral position after transport or manual handling.

<img src="12-admin/02-panel-en.png" width="700">

## Withheld

19 captures show real participant names, identifiers
or e-mail addresses and are held out of this repository until they are
recaptured with synthetic data.

