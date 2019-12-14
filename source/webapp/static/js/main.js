const baseUrl = 'http://localhost:8000/api/v1/';

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


function commentAdd(){
    let addBtn= $('#comment_add');
    console.log(addBtn.attr('data-photo-id'));
    let token = getCookie('csrftoken');
    $.ajax({
      type: "POST",
      url: baseUrl + 'comment/',
      data: JSON.stringify(
          {
              image : addBtn.attr('data-photo-id'),
              author : addBtn.attr('data-author-id'),
              text: $('#author-text').val()
          }
      ),
      dataType: 'json',
      contentType: 'application/json',
      headers: {
         'X-CSRFToken': token
      },
      success: function (response) {
          let new_comment = `<div class="body${response.comment_id}">
                            <p>
                                <b>Автор:</b>${addBtn.attr('data-author-id')}
                                <b>Created at:</b> ${response.created_at}
                            </p>
                            <div class="pre">
                                Текст : ${$('#author-text').val()}
                            </div>
                            <p class="comment-links">
                                <a href="">Edit</a>
                                <a href="">Delete</a>
                            </p>             
                        </div>`;
        $('#comment-list').append(new_comment);
      }
    });
}



$(document).ready(function() {
    getCookie();
    commentAdd();
});