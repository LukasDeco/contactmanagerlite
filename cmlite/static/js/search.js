/*$("form#searchform input").keyup(function() {
  $('.contact_list').html('<div class="loader"></div>');
});*/

$(document).on('click', '.contact_list .contact-header', function(){
  $(this).parent('.contact-demo').toggleClass('collapsed');
});

$("form#searchform input").keyup(function () {
      $('.contact_list').html('<div class="loader"></div>');
     var first_name = $('input#first_name').val();
     var last_name = $('input#last_name').val();
     var phone_number = $('input#phone_number').val();
     var email_address = $('input#email_address').val();
     var csrf = $('input[name=csrfmiddlewaretoken]').val();
     $.ajax({
       type: 'POST',
       url: 'quick_search/',
       data: {
         'first_name': first_name,
         'last_name': last_name,
         'phone_number': phone_number,
         'email_address': email_address,
         'csrfmiddlewaretoken': csrf
       },
       dataType: 'html',
       error: function (data) {
         console.log(data);
       },
       success: function (data) {
         if (!$.trim(data)) {
            $('.contact_list').html('<div class="messages"><span>No contacts found..</span></div>');
         }
         else {
         $('.contact_list').html(data);
       }
       }

     });

   });
