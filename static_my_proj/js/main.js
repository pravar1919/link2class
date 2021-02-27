

$( document ).ready(function() {
    $('.like-form').submit(function(e){
        e.preventDefault()
        
        const post_id = $(this).attr('id')
        
        const likeText = $(`.like-btn${post_id}`).text()
        const trim = $.trim(likeText)

        const url = $(this).attr('action')
        
        let res;
        const likes = $(`.like-count${post_id}`).text()
        const trimCount = parseInt(likes)
        
        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'post_id':post_id,
            },
            success: function(response) {
              // var submitSpan = $(".submit-span")
    // console.log('success');
                if(trim === 'Unlike') {
                  // submitSpan.html("<i class="fa fa-thumbs-up text_blue" aria-hidden="true"></i>")
                    $(`.like-btn${post_id}`).text('Like')
                    res = trimCount - 1
                } else {
                  // submitSpan.html("<i class="fa fa-thumbs-down text_blue" aria-hidden="true"></i>")
                    $(`.like-btn${post_id}`).text('Unlike')
                    res = trimCount + 1
                }

                $(`.like-count${post_id}`).text(res)
            },
            error: function(response) {
                console.log('error', response)
                window.location.href = '/users/login/';
            }
        })

    })
    $("#login-form").submit(function (e) {
        e.preventDefault();
        var serializedData = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: "/accounts/login/",
            data: serializedData,
            success: function (response) {
                window.location.href= "/";
            },
            error: function (response) {
                // alert the error if any error occured
                alert("Email or password is wrong");
            }
        })
    });
});