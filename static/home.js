$(document).keydown( function(event) {
    if (event.which === 87) {
        $.getJSON('/up',
        function(data) {
        //do nothing
        });
        return false;
    }
    if (event.which === 32) {
        $.getJSON('/stop',
        function(data) {
        //do nothing
        });
        return false;
    }
    if (event.which === 65) {
        $.getJSON('/left',
        function(data) {
        //do nothing
        });
        return false;
    }
    if (event.which === 83) {
        $.getJSON('/down',
        function(data) {
        //do nothing
        });
        return false;
    }
    if (event.which === 68) {
        $.getJSON('/right',
        function(data) {
        //do nothing
        });
        return false;
    }
  }); 
// document.getElementById("controller")
//     .addEventListener("keyup", function(e) {
//     if (e.code === 'KeyA') {
//         document.getElementById("left").click();
//     }
//     if (e.code === 'KeyW') {
//         document.getElementById("up").click();
//     }
//     if (e.code === 'KeyS') {
//         document.getElementById("down").click();
//     }
//     if (e.code === 'KeyD') {
//         document.getElementById("right").click();
//     }
// });

$(function() {
    $('a#up').on('click', function(e) {
      e.preventDefault()
      $.getJSON('/up',
          function(data) {
        //do nothing
      });
      return false;
    });
  });

  $(function() {
    $('a#down').on('click', function(e) {
      e.preventDefault()
      $.getJSON('/down',
          function(data) {
        //do nothing
      });
      return false;
    });
  });

  $(function() {
    $('a#left').on('click', function(e) {
      e.preventDefault()
      $.getJSON('/left',
          function(data) {
        //do nothing
      });
      return false;
    });
  });

  $(function() {
    $('a#right').on('click', function(e) {
      e.preventDefault()
      $.getJSON('/right',
          function(data) {
        //do nothing
      });
      return false;
    });
  });

  $(function() {
    $('a#stop').on('click', function(e) {
      e.preventDefault()
      $.getJSON('/stop',
          function(data) {
        //do nothing
      });
      return false;
    });
  });