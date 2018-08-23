$('input').keyup( function() {
  new_fn = $('input#id_first_name').val();
  new_ln = $('input#id_last_name').val();
  new_pn = $('input#id_phone_number').val();
  new_ea = $('input#id_email_address').val();
  $('.contact-demo').removeClass('hidden');
  $('.contact-demo .initials').html(new_fn.concat(" " + new_ln));
  $('.contact-demo #fn-input').val(new_fn);
  $('.contact-demo #ln-input').val(new_ln);
  $('.contact-demo #pn-input').val(new_pn);
  $('.contact-demo #ea-input').val(new_ea);
});
