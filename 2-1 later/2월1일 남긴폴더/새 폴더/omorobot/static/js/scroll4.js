$(window).scroll((e) => {
  console.log($(window).scrollTop())

  if($(window).scrollTop() < 200) {
    $(".explain_b").hide()
  } else if($(window).scrollTop() > 4800) {
    $(".explain_b").fadeIn(1500)
  } 
});
