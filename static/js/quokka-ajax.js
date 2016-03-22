$('.up').click(function(){
    var aid = $(this).attr("data-aid");
    var score = 1;
    $.get('/quokka/vote_on_answer/', {answer_id: aid, score: score}, function(data){
		var current_score = $('#a-'+aid+' .score').html();
		$('#a-'+aid+' .score').html(parseInt(current_score)+1)
		$('#up').hide();
    });
});

$('.down').click(function(){
    var aid = $(this).attr("data-aid");
    var score = -1
    $.get('/quokka/vote_on_answer/', {answer_id: aid, score: score}, function(data){
       var current_score = $('#a-'+aid+' .score').html();
		$('#a-'+aid+' .score').html(parseInt(current_score)-1)
		$('#down').hide();
    });
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
            }
        }
    }
    return cookieValue;
}

$('.answer.form button').on('click', function(e) {
    console.log("Clicked submit in form");

    // prevetn default submit
    e.preventDefault();

    var qid = $(this).attr("data-qid"); // gets ID of question being answered
    var text = $(this).parent().find('textarea').val(); // gets text of answer to question
    console.log(qid);
    console.log(text);

    // get CSRF token and log it
    var csrftoken = getCookie('csrftoken');
    console.log(csrftoken);

    // now to submit answer
    $.ajax({
            url : 'answer_question/', // the endpoint, commonly same url
            type : "POST", // http method
            data : {
                csrfmiddlewaretoken : csrftoken, 
                question_id : qid,
                text : text
            }, // data sent with the post request
            success : function(data) {
                //On success show the data posted to server as a message
                console.log(data);

                //var x = data.split('|');

                //console.log(x);

                // var qid = x[0];
                // var aid = x[1];
                // var text = x.slice(2).join("|");

                // var newAnswer = "<li class='answer' id='a-" + aid + "'>" + 
                //                     "<div class='votes'>" + 
                //                         "<div class='score'>0</div>" + 
                //                     "</div>" + 
                //                     "<div class='text'>" + 
                //                         "<span>" + text + "</span>" + 
                //                         "<p class='username'>" + "[user]" + "</p>" + // TODO: username
                //                     "</div>" + 
                //                 "</li>";
                // $('li#q-' + qid + ' ul.answers').prepend(newAnswer);
            },
            // handle a non-successful response
            error : function(xhr, errmsg, err) {
                // provide a bit more info about the error to the console
                console.log("Failed AJAX POST");
            }
     });
});