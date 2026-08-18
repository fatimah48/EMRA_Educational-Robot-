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
<td width="50%"><img src="docs/interfaces/01-talk/02-talk-boy-en.png" width="100%"><br><sub>Talk with EMRA using the boy interface. The child can interact in English, Arabic, or automatic language detection mode.</sub></td>
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
<td width="50%"><img src="docs/interfaces/02-body-parts/04-body-memory-en.png" width="100%"><br><sub>Body Parts Memory. The child observes a body-part sequence and then reproduces it from memory in the correct order.</sub></td>
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

This section includes two activities: **Word Tracing** and **Spelling**.

**Word Tracing** asks the child to trace words using a faded guide inside the writing area. Each letter fills with color as it is completed. The activity includes separate English and Arabic word sets.

**Spelling** shows a picture and asks the child to arrange letter tiles in the correct order to build the corresponding word.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/08-writing/00-menu-en.png" width="100%"><br><sub>Entry screen for Word Tracing and Spelling.</sub></td>
<td width="50%"><img src="docs/interfaces/08-writing/01-tracing-level-select-en.png" width="100%"><br><sub>Word Tracing level selection with three levels.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/08-writing/02-tracing-start-en.png" width="100%"><br><sub>Word Tracing before the first stroke, with the guide word shown inside the writing area.</sub></td>
<td width="50%"><img src="docs/interfaces/08-writing/03-tracing-progress-en.png" width="100%"><br><sub>Tracing in progress as the completed letters fill with color.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/08-writing/04-tracing-success-en.png" width="100%"><br><sub>Completion feedback after successfully tracing the word.</sub></td>
<td width="50%"><img src="docs/interfaces/08-writing/05-tracing-level-select-ar.png" width="100%"><br><sub>Arabic Word Tracing level selection.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/08-writing/06-tracing-progress-ar.png" width="100%"><br><sub>Arabic Word Tracing in progress.</sub></td>
<td width="50%"><img src="docs/interfaces/08-writing/07-spelling-level-select-en.png" width="100%"><br><sub>Spelling level selection with four levels.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/08-writing/08-spelling-gameplay-en.png" width="100%"><br><sub>Spelling activity. The child arranges letter tiles to build the pictured word.</sub></td>
<td width="50%"><img src="docs/interfaces/08-writing/09-spelling-success-en.png" width="100%"><br><sub>Completion feedback with the correctly spelled word.</sub></td>
</tr>
</table>

## Reading

The Reading activity provides three short illustrated stories. Each story is
narrated sentence by sentence while the currently spoken word is highlighted,
helping the child follow the written text during narration. Pages are advanced
manually so the child can remain on each page as needed.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/09-reading/01-contents-en.png" width="100%"><br><sub>Story selection screen with three illustrated stories.</sub></td>
<td width="50%"><img src="docs/interfaces/09-reading/02-story-star-en.png" width="100%"><br><sub>Story narration with the currently spoken word highlighted in the text.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/09-reading/03-story-seed-en.png" width="100%"><br><sub>Another story page with manual page navigation.</sub></td>
<td></td>
</tr>
</table>

## Letters

This section includes two activities: **Letter Garden** and **Letter Tracing**.

**Letter Garden** asks the child to identify a spoken letter by selecting the matching tile. A correct choice grows the flower and presents an example word that begins with the selected letter.

**Letter Tracing** asks the child to trace the shape of a letter using a dotted guide and marked starting point.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/10-letters/00-menu-en.png" width="100%"><br><sub>Entry screen for Letter Garden and Letter Tracing.</sub></td>
<td width="50%"><img src="docs/interfaces/10-letters/01-flower-start-en.png" width="100%"><br><sub>Letter Garden. The child hears a letter and selects the matching tile.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/10-letters/02-flower-letter-a-en.png" width="100%"><br><sub>Correct selection. The flower grows and an example word beginning with the letter is presented.</sub></td>
<td width="50%"><img src="docs/interfaces/10-letters/04-tracing-a-start-en.png" width="100%"><br><sub>Letter Tracing with a dotted guide and marked starting point.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/10-letters/05-tracing-a-success-en.png" width="100%"><br><sub>Completion feedback after successfully tracing the letter.</sub></td>
<td></td>
</tr>
</table>

## Educator dashboard

The educator dashboard presents child-level and group-level performance from the recorded activity sessions. For each child, it summarizes measures such as accuracy, response time, attempts, help usage, level reached, and stars earned across activities.

The dashboard also provides group comparisons and generates written progress reports from the recorded data. Talk sessions are reported separately, including session duration and turn count, with conversation reports generated from selected sessions and optionally sent by email.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/01-children-list-en.png" width="100%"><br><sub>List of enrolled children with their activity progress.</sub></td>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/02-child-summary-en.png" width="100%"><br><sub>Individual child summary with performance measures across activities.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/03-visual-analysis-top-en.png" width="100%"><br><sub>Visual summary of the selected child's recorded activity performance.</sub></td>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/05-accuracy-by-subject-en.png" width="100%"><br><sub>Accuracy across activities.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/06-response-time-en.png" width="100%"><br><sub>Mean response time across activities.</sub></td>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/07-stars-earned-en.png" width="100%"><br><sub>Stars earned across activities.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/08-class-overview-en.png" width="100%"><br><sub>Group overview with overall performance measures.</sub></td>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/09-accuracy-by-student-en.png" width="100%"><br><sub>Accuracy comparison across children.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/10-students-table-en.png" width="100%"><br><sub>Group performance table with sortable measures.</sub></td>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/12-llm-report-body-en.png" width="100%"><br><sub>Generated progress report summarizing strengths, difficulties, and suggested next steps.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/14-talk-sessions-en.png" width="100%"><br><sub>Recorded Talk sessions with duration, turn count, and session status.</sub></td>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/17-talk-report-body-en.png" width="100%"><br><sub>Generated Talk report summarizing the selected conversation sessions.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/interfaces/11-educator-dashboard/18-talk-report-emailed-en.png" width="100%"><br><sub>Confirmation after sending the generated report by email.</sub></td>
<td></td>
</tr>
</table>

## Administrator panel

Maintenance functions are available through an administrator sign in. The panel
restores the head servos to their neutral position on each rotation axis, which
is useful after transport or when the head has been moved manually.

<table>
<tr>
<td width="50%"><img src="docs/interfaces/12-admin/01-login-en.png" width="100%"><br><sub>Administrator sign in, which keeps maintenance functions unavailable during a child session.</sub></td>
<td width="50%"><img src="docs/interfaces/12-admin/02-panel-en.png" width="100%"><br><sub>Head servo calibration. Each rotation axis can be returned to its neutral position after transport or manual handling.</sub></td>
</tr>
</table>
