<h1 align="center">EMRA: Educational Multimodal Robot Assistant</h1>
<p align="center">A bilingual Arabic and English social robot for children with autism spectrum disorder.</p>

<p align="center">
  <img src="docs/interfaces/00-overview/00-main-menu-en.png" width="85%">
</p>

EMRA runs an activity suite on a touchscreen mounted on the robot's chest, with
an animated face on a circular head display. A conversational track listens to
the child, reads emotion from both speech and facial expression, and replies in
the language of the session. Ten activities cover conversation, body awareness,
puzzles, LEGO, painting, colors, numbers, writing, reading, and letters.
An educator view reports progress per child and per
group, and generates written progress notes.The robot shown below:

<p align="center">
  <img src="docs/interfaces/emra.jpg" alt="EMRA Robot" width="450">
</p>



Every screen below is from the deployed system.

---

## Overview and session start

The educator starts a session by entering the child’s name, age, identifier, and gender, or continues as a guest when no record is needed. Activity data from the session are logged and later presented in the educator dashboard.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/00-overview/01-session-start-validation-en.png" width="100%"><br><sub>The session start panel rejects an empty form, so a child record or an explicit guest choice is always made before an activity opens.</sub></td>
<td width="50%"><img src="docs/interfaces/00-overview/02-session-start-filled-en.png" width="100%"><br><sub>Session start completed. Name, age, identifier and gender are bound to every record the session produces.</sub></td>
</tr>
</table>

## Talk with EMRA

The child speaks with EMRA in an open conversation. Speech is transcribed, text and facial emotions are fused, and the resulting emotion is used to adapt the LLM-generated response and the robot's facial expression. When visual grounding is triggered, the VLM describes the relevant object or scene and the LLM uses that description to generate the final response.

The interface adapts to the child's selected gender, displaying either the girl or boy version while keeping the same conversational functions and language options.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/01-talk/01-talk-girl-en.png" width="100%"><br><sub>Talk with EMRA using the girl interface. The child can interact in English, Arabic, or automatic language detection mode.</sub></td>
<td width="50%"><br><br><em>Boy interface screenshot will be added here.</em><br><br></td>
</tr>
</table>

## Body parts

This section includes two bilingual activities: **Body Explorer** and **Body Parts Memory**.

**Body Explorer** teaches the child to identify facial parts and the hand. The child sees a mirrored camera view and responds to spoken and visual prompts by pointing to the requested part. Face and hand landmark detection are used to track the relevant facial regions and the child’s fingertip. A response is accepted when the child points to the correct part for a short period.

**Body Parts Memory** adds a memory task using the same camera-based interaction. The child first watches a sequence of body parts and then reproduces the sequence from memory by pointing to them in the correct order. The sequence becomes longer across four levels, increasing from one body part to four.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/02-body-parts/01-activity-menu-en.png" width="100%"><br><sub>Body Parts menu with the Body Explorer and Body Parts Memory activities.</sub></td>
<td width="50%"><img src="docs/interfaces/02-body-parts/02-body-explorer-intro-en.png" width="100%"><br><sub>Body Explorer introduces the facial and hand parts used in the activity.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/02-body-parts/03-body-explorer-camera-en.png" width="100%"><br><sub>Camera-based interaction in Body Explorer. The child points to the requested body part while the system tracks the response.</sub></td>
<td width="50%"><br><br><em>Body Parts Memory screenshot will be added here.</em><br><br></td>
</tr>
</table>

## Puzzle

The Puzzle activity supports visual matching and spatial reasoning through four
progressively harder levels. The child reconstructs a reference image by placing
the puzzle pieces in the correct positions, with the number of pieces increasing
from two to nine. The reference picture can be shown when needed. Levels unlock
in order, while Free Play allows available puzzles to be replayed without the
level progression.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/03-puzzle/01-level-select-en.png" width="100%"><br><sub>Level selection. Four levels are unlocked in order, with the number of pieces increasing from two to nine.</sub></td>
<td width="50%"><img src="docs/interfaces/03-puzzle/02-level-select-ar.png" width="100%"><br><sub>The same level-selection screen in Arabic with a right-to-left layout.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/03-puzzle/03-gameplay-bus-en.png" width="100%"><br><sub>Level one with two pieces. The reference picture can be viewed when needed.</sub></td>
<td width="50%"><img src="docs/interfaces/03-puzzle/04-completion-bus-en.png" width="100%"><br><sub>Completion feedback shown after solving the puzzle.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/03-puzzle/06-gameplay-friends-en.png" width="100%"><br><sub>Level three with six pieces and the remaining pieces displayed below the board.</sub></td>
<td width="50%"><img src="docs/interfaces/03-puzzle/07-free-play-en.png" width="100%"><br><sub>Free Play allows available puzzles to be replayed without the level progression.</sub></td>
</tr>
</table>

## LEGO build

The LEGO activity supports visual construction and color matching. The child
reproduces a target model by dragging colored bricks from the tray onto the
building grid. Nine target models are provided with increasing complexity.

In **Levels** mode, the builds unlock progressively as each model is completed.
**Free Build** allows the child to choose any of the available target models.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/04-lego/01-level-select-en.png" width="100%"><br><sub>Level Mode</sub></td>
<td width="50%"><img src="docs/interfaces/04-lego/02-gameplay-tree-en.png" width="100%"><br><sub>Free Play</sub></td>
</tr>
</table>

## Painting

The Painting activity provides seven coloring templates. The child
selects a crayon and colors different regions of the picture. A reference
image is available for guidance and can be shown or hidden during the activity.

The templates include a rainbow, number, duck, turtle, elephant, house, and
ice cream, providing different shapes and levels of visual detail.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/05-painting/01-rainbow-en.png" width="100%"><br><sub>Rainbow coloring template with the crayon palette and reference image.</sub></td>
<td width="50%"><img src="docs/interfaces/05-painting/05-elephant-en.png" width="100%"><br><sub>Elephant template with multiple regions available for coloring.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/05-painting/07-ice-cream-en.png" width="100%"><br><sub>Ice cream template, one of the seven available pictures.</sub></td>
<td></td>
</tr>
</table>

## colors

This section includes two activities: **Color Match** and **Color Discovery**.

**Color Match** asks the child to match each named crayon to its corresponding color. Correct matches earn stars, while repeated incorrect attempts trigger a visual hint.

**Color Discovery** presents eleven colors with their written and spoken names. Selecting a color plays a short animation and displays the color word, linking the color with its written and spoken form.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/06-colors/01-menu-en.png" width="100%"><br><sub>Entry screen for the Color Match and Color Discovery activities.</sub></td>
<td width="50%"><img src="docs/interfaces/06-colors/02-match-gameplay-en.png" width="100%"><br><sub>Color Match. The child matches each named crayon to its corresponding color.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/06-colors/03-match-complete-en.png" width="100%"><br><sub>Completion feedback after all color pairs are matched.</sub></td>
<td width="50%"><img src="docs/interfaces/06-colors/04-discover-board-en.png" width="100%"><br><sub>Color Discovery presents eleven colors that can be selected individually.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/06-colors/05-reveal-animation-en.png" width="100%"><br><sub>Animation shown after a color is selected.</sub></td>
<td width="50%"><img src="docs/interfaces/06-colors/06-word-reveal-en.png" width="100%"><br><sub>The selected color is presented with its written and spoken name.</sub></td>
</tr>
</table>

## Numbers

This section includes two activities: **Number Tracing** and **Bubble Count**.

**Number Tracing** asks the child to trace a numeral using a dotted guide and marked starting point, with spoken feedback during the activity.

**Bubble Count** asks the child to count the bubbles shown on the screen and select the matching number.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/07-numbers/00-menu-en.png" width="100%"><br><sub>Entry screen for Number Tracing and Bubble Count.</sub></td>
<td width="50%"><img src="docs/interfaces/07-numbers/01-tracing-one-start-en.png" width="100%"><br><sub>Number Tracing with a dotted guide and marked starting point.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/07-numbers/02-tracing-one-success-en.png" width="100%"><br><sub>Completion feedback after successfully tracing the numeral.</sub></td>
<td width="50%"><img src="docs/interfaces/07-numbers/03-listen-find-one-en.png" width="100%"><br><sub>Bubble Count. The child counts the bubbles and selects the matching number.</sub></td>
</tr>
</table>

## Writing

Handwriting and spelling. Word tracing shows a faded guide word inside the
writing area and fills each letter in color as it is traced, in English and in
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
<td width="50%"><img src="docs/interfaces/08-writing/03-tracing-progress-en.png" width="100%"><br><sub>Tracing in progress. Each letter fills with color as it is completed.</sub></td>
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
