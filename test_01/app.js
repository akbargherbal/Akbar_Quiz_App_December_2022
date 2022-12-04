let x = 'a bunch of text here and there'.split('');

function makeForm (array_01, form_id) {
    for (var i = 0; i < array_01.length; i++) {
        var input = document.createElement("input");
        input.type = "text";
        input.value = array_01[i];
        input.id = "input_" + (i+1);
        document.getElementById(form_id).appendChild(input);
    }
}

makeForm(x, 'form_01');