console.log("entered quokka-ajeeeeex file");

$('.up').click(function(){
	console.log("entered function on 'up' click");
	console.log(this);
    var aid = $(this).attr("data-aid");
    var score = 1;
    $.get('/quokka/vote_on_answer/', {answer_id: aid, score: score}, function(data){
               //$('#score').html(data);
               $('#up').hide();
    });
});

$('.down').click(function(){
	console.log("entered function on 'down' click");
	console.log(this);
    var aid = $(this).attr("data-aid");
    var score = -1
    $.get('/quokka/vote_on_answer/', {answer_id: aid, score: score}, function(data){
               //$('#score').html(data);
               $('#down').hide();
    });
});