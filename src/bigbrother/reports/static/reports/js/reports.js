$(function() {
    $('a.fav').click(function(e) {
        e.preventDefault();
        var studentID = parseInt($(this).data('id'), 10);
        var eventID = parseInt($(this).data('id'), 10);
        var doToggle = toggleFavourite(pensionID);
        if (doToggle) {
            $(this).find('span').toggleClass('is-fav');
        }
        return false;
    });

	function addAbsence() {
        var data = JSON.stringify({
            "event": "1",
            "student": "2",
            "excuse": "another-post"
        });

        $.ajax({
          url: 'http://localhost:8000/api/v1/absence/',
          type: 'POST',
          contentType: 'application/json',
          data: data,
          dataType: 'json',
          processData: false
        })
	}
});