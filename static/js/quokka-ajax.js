console.log("entered quokka-ajeeeeex file");

$('.up').click(function(){
	console.log("entered function on 'up' click");
	console.log(this);
    var aid = $(this).attr("data-aid");
    var score = 1;
    $.get('/quokka/vote_on_answer/', {answer_id: aid, score: score}, function(data){
				var current_score = $('#a-'+aid+' .score').html();
				$('#a-'+aid+' .score').html(parseInt(current_score)+1)
				$('#up').hide();
    });
});

$('.down').click(function(){
	console.log("entered function on 'down' click");
	console.log(this);
    var aid = $(this).attr("data-aid");
    var score = -1
    $.get('/quokka/vote_on_answer/', {answer_id: aid, score: score}, function(data){
               var current_score = $('#a-'+aid+' .score').html();
				$('#a-'+aid+' .score').html(parseInt(current_score)-1)
				$('#down').hide();
    });
});