# Activity introductions

Prose shown above each section of the interface gallery. Edit the text here,
then run `organize_interfaces.py` to rebuild `docs/interfaces/README.md`.
Each block starts with `## <folder-name>` on its own line. Everything until the
next `##` is the introduction for that folder.

## 00-overview

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

## 01-talk

Open conversation with EMRA. The child speaks, the robot listens, replies and
responds with a facial expression. This is the only activity that routes
through the language model. Speech is transcribed, emotion is read from both
the transcript and the child's face, the two channels are fused, and the fused
signal conditions the reply and the expression the robot shows. The
educational games are entirely separate from this track and never call the
language model.

## 02-body-parts

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

## 03-puzzle

Visual matching and spatial reasoning. Four pictures are offered across four
levels, with the piece count rising from two to six. The reference picture can
be shown on demand. Levels unlock in order, and a free play mode lets the child
replay anything already unlocked without the level gate.

## 04-lego

Block construction against a target model. The target is displayed beside an
empty grid and the child drags bricks from the tray to reproduce it. Eight
models are available, ordered by the number of bricks and the number of
distinct colours involved.

## 05-painting

Colour by number. Each template pairs a line drawing with a numbered key, and
the child selects the crayon whose number matches the region. The reference
image stays visible for comparison. Seven templates run from five regions to
eight, so difficulty rises through both region count and region size.

## 06-colors

Two colour activities. The matching game asks the child to connect each named
crayon to its swatch, which tests colour naming rather than colour perception
alone. The discovery board presents eleven colour names, speaks each one, and
plays a short fill animation with the written word so the spoken name, the
written name and the colour are presented together.

## 07-numbers

Early numeracy in two forms. Numeral tracing shows a dotted guide with a marked
starting point and speaks the number name as the stroke is completed. The
listening task speaks a number and asks the child to find it among floating
bubbles, which separates recognising the spoken word from producing the shape.

## 08-writing

Handwriting and spelling. Word tracing shows a faded guide word inside the
writing area and fills each letter in colour as it is traced, in English and in
Arabic. The Arabic levels use connected letter forms with diacritics, so the
task is not a mirror of the English one. The spelling activity shows a picture
and asks the child to place letter tiles in order to build the word.

## 09-reading

Shared reading. Three short illustrated stories are narrated sentence by
sentence with the spoken word highlighted in the text, so the child follows the
written form while hearing it. Pages advance manually, which lets an educator
hold on a page for as long as the child needs.

## 10-letters

Letter work in two forms. In the recognition game the child picks a letter
tile from a row and a correct choice grows a flower and speaks an example word
beginning with that letter. Letter tracing then asks the child to produce the
shape, using the same dotted guide and start marker as the numeral task.

## 11-educator-dashboard

The educator view, reached from a separate entry point on the main menu. For a
single child it reports accuracy, mean response time, attempts, help usage,
level reached and stars earned, broken down by activity. For the cohort it
ranks children on the same measures. A report generator turns the logged
records into written progress notes in English or Arabic covering strengths,
difficulties and suggested next steps. Conversation sessions from the Talk
activity are listed separately with turn counts and duration, and a report can
be generated over selected sessions and e-mailed to the educator.

## 12-admin

Maintenance functions behind an administrator sign in. The panel restores the
head servos to their neutral position on each rotation axis, which is needed
after transport or after a session in which the head was moved by hand.
