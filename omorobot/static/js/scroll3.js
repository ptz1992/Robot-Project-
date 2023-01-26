$(window).scroll((e) => {
  console.log($(window).scrollTop())

  if($(window).scrollTop() < 200) {
    $(".explain_a_2").hide()
  } else if($(window).scrollTop() > 3800) {
    $(".explain_a_2").fadeIn(1500)
  } 
});

