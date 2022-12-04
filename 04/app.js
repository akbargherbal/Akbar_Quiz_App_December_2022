const quiz_set = [{"QUESTION_TEXT":"\"Yes. At two. With Amanda. Thanks for-\" lightning f _ _ _ _ d overhead and she cringed, but this time it was more diffuse, and the thunder which followed, while loud, didn't threaten to burst her eardrums. \"-for being so understanding,\" [6 Letters F _ _ _ _ _ D]","OPTION_1":"flared","OPTION_2":"FLARED","OPTION_3":"Flared"},{"QUESTION_TEXT":"I mostly k _ _ _  my eyes closed, feeling ahead of me with my hands, because even in the pitch darkness, as long as my eyes were open, my mind kept wanting to see, and tended to panic when it couldn't. [4 Letters K _ _ _ ]","OPTION_1":"kept","OPTION_2":"KEPT","OPTION_3":"Kept"},{"QUESTION_TEXT":"\"I brought McNab,\" Peabody told her. \"He and Roarke are taking the electronics. Roarke's already gone over the front entrance. No sign of f _ _ _ _ d entry. According to the expert, whoever brought him in used the proper swipe, the code, the works.\" [6 Letters F _ _ _ _ _ D]","OPTION_1":"forced","OPTION_2":"FORCED","OPTION_3":"Forced"},{"QUESTION_TEXT":"His mother cried, emitting no sounds as she slowly shook her head back and forth, as if not yet able to a _ _ _ _ b what he had done. [6 Letters A _ _ _ _ _ B]","OPTION_1":"absorb","OPTION_2":"ABSORB","OPTION_3":"Absorb"},{"QUESTION_TEXT":"I've organized a search party, and we're about to h _ _  the streets\"-when the phone rang. His father grabbed it, offered his usual gruff \"Woods Boone,\" then began listening. [3 Letters H _ _ _ ]","OPTION_1":"hit","OPTION_2":"HIT","OPTION_3":"Hit"},{"QUESTION_TEXT":"I opened my mouth to s _ _  Maeve Reed's name, but stopped myself. My aunt was the Queen of Air and Darkness; anything said in the dark would eventually travel back to her. [3 Letters S _ _ _ ]","OPTION_1":"say","OPTION_2":"SAY","OPTION_3":"Say"},{"QUESTION_TEXT":"She paused as an enormous wave of relief w _ _ _ _ d over her. \"Only Amy wasn't wearing a hat.\" [6 Letters W _ _ _ _ _ D]","OPTION_1":"washed","OPTION_2":"WASHED","OPTION_3":"Washed"},{"QUESTION_TEXT":"It was just before lunch, and Olive would be packed with people t _ _ _ _ g to shove food in their mouths and rush back to work. [6 Letters T _ _ _ _ _ G]","OPTION_1":"trying","OPTION_2":"TRYING","OPTION_3":"Trying"},{"QUESTION_TEXT":"\"Stick with me, kid.\" She stopped at the top curve of the stairs. \"Let's make an entrance. Chins up, eyes bored, stomachs in, fingers t _ _ _ _ _ _ g carelessly along the banisters.\" [8 Letters T _ _ _ _ _ G]","OPTION_1":"trailing","OPTION_2":"TRAILING","OPTION_3":"Trailing"},{"QUESTION_TEXT":"We all trooped up to the house and knocked on the door. Uncle Vito's wife, Aunt Angela, o _ _ _ _ d the door. [6 Letters O _ _ _ _ _ D]","OPTION_1":"opened","OPTION_2":"OPENED","OPTION_3":"Opened"},{"QUESTION_TEXT":"He'd lost his right shoe near the perimeter going in, with no way to retrieve it except by hand, a process about as attractive as bobbing for turds, and likely to a _ _ _ _ _ t the attention of the Black Karens. [7 Letters A _ _ _ _ _ T]","OPTION_1":"attract","OPTION_2":"ATTRACT","OPTION_3":"Attract"},{"QUESTION_TEXT":"The sounds c _ _ _ _ g through the door were faint and muffled. Davos rose and paced his cell. As cells went, it was large and queerly comfortable. He suspected it might once have been some lordling's bedchamber. [6 Letters C _ _ _ _ _ G]","OPTION_1":"coming","OPTION_2":"COMING","OPTION_3":"Coming"},{"QUESTION_TEXT":"\"Because she thinks if she keeps buying it, she'll have to eat it just to G _ _  rid of it. It's like she's trying to trick herself.\" [3 Letters G _ _ _ ]","OPTION_1":"get","OPTION_2":"GET","OPTION_3":"Get"},{"QUESTION_TEXT":"The attorney's admission surprised Junior. This was probably as close as Magusson would ever get to saying, Maybe you didn't k _ _ _  your wife, after all, but he was by nature a nasty prick, so even an implied apology was more than Junior had ever expected to receive. [4 Letters K _ _ _ ]","OPTION_1":"kill","OPTION_2":"KILL","OPTION_3":"Kill"},{"QUESTION_TEXT":"\"They keep each other on their toes. It's fun to w _ _ _ h.\" [5 Letters W _ _ _ _ _ H]","OPTION_1":"watch","OPTION_2":"WATCH","OPTION_3":"Watch"},{"QUESTION_TEXT":"I showed her my badge and t _ _ _  her my name, and she said her name was Marilyn Burns. She was forty, white, and petite and dressed in a blue-checked shirt hanging out over her jeans. [4 Letters T _ _ _ ]","OPTION_1":"told","OPTION_2":"TOLD","OPTION_3":"Told"},{"QUESTION_TEXT":"\"But know that I can t _ _ _  your head before you blink if you so much as think of harming her.\" [4 Letters T _ _ _ ]","OPTION_1":"take","OPTION_2":"TAKE","OPTION_3":"Take"},{"QUESTION_TEXT":"That even though he had no idea what he was praying about, he wanted to m _ _ _  sure that the Oversoul understood that he was serious. [4 Letters M _ _ _ ]","OPTION_1":"make","OPTION_2":"MAKE","OPTION_3":"Make"},{"QUESTION_TEXT":"LuAnn held onto the sides of her seat and gritted her teeth as the plane rocked and swayed while it g _ _ _ _ _ _ d speed. She didn't dare look outside the window. Oh Lord, what had she done? [8 Letters G _ _ _ _ _ D]","OPTION_1":"gathered","OPTION_2":"GATHERED","OPTION_3":"Gathered"},{"QUESTION_TEXT":"Rose gasped, t _ _ _ _ d from the door, and pressed her gaze upon the ceiling again as if it might crash down on them. [6 Letters T _ _ _ _ _ D]","OPTION_1":"turned","OPTION_2":"TURNED","OPTION_3":"Turned"}]
const quiz_length = quiz_set.length;

const ui_start = document.getElementById('start_game')
const ui_quiz_container = document.getElementById('quiz_container')
const ui_question_text = document.getElementById('question_text')
const ui_quiz_no = document.getElementById('quiz_no')

const ui_correct_answers = document.getElementById('correct_answers')
const ui_wrong_answers = document.getElementById('wrong_answers')
const ui_score = document.getElementById('score')


const ui_answer_text = document.getElementById('answer_area')
const ui_submit_answer = document.getElementById('submit_button')

var quiz_number = 0
var choices;

var correct_answers = 0;
var wrong_answers = 0;
var score = 0;


ui_start.addEventListener('click', startGame)
ui_submit_answer.addEventListener('click', submitAnswer)

ui_answer_text.addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.key === "Enter") {
        ui_submit_answer.click();
    }
  });




function startGame() {
    console.log('Game Started')
    ui_start.classList.add('hide')
    ui_quiz_container.classList.remove('hide')
    makeQuiz()
}

function gameOver() {
    console.log('Game Over')
    ui_quiz_container.classList.add('hide')    
}

function makeQuiz() {
    if (quiz_set.length > 0) {
        let currenQuiz = quiz_set.shift();
        quiz_number = quiz_number + 1;

        ui_quiz_no.textContent = `Question ${quiz_number} of ${quiz_length}`;
        ui_question_text.textContent = currenQuiz.QUESTION_TEXT;

        choices = [currenQuiz.OPTION_1, currenQuiz.OPTION_2, currenQuiz.OPTION_3]
    } else {gameOver()}
    

}

function submitAnswer() {
    ui_answer_text.classList.remove('answer_correct')
    ui_answer_text.classList.remove('answer_incorrect')
    let answer = ui_answer_text.value
    console.log(`Answer in Text Area: ${answer}`)
    if (choices.includes(answer)) {
        console.log('Correct', `Indeed ${answer} is one of the choices in ${choices}`)
        correct_answers = correct_answers + 1;
    } else {console.log('WRONG;', `Answer ${answer} is not one of the choices in ${choices}`)
            wrong_answers = wrong_answers + 1;}
    score = Math.floor(100 * ((correct_answers)/(correct_answers + wrong_answers)));

    ui_correct_answers.textContent = `Correct Answers: ${correct_answers}`
    ui_wrong_answers.textContent = `Wrong Answers: ${wrong_answers}`
    ui_score.textContent = `Score: ${score}%`
    ui_answer_text.value = ''
    makeQuiz()
}