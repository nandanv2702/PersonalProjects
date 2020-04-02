  $(document).ready(function(){
    $(".board").mousemove(function(){
      if($(".item:hover").length != 0){
        console.log($(".item:hover").innerHTML);
      }
      else {
        console.log("none")
      }
    });
  })
