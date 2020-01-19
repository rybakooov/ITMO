$(document).ready(function(){
 /* $.ajax({
    type: "GET",  
	  url: "temp.csv",
	  dataType: "text",       
	  success: function(response)  
	  {
      data = $.csv.toArrays(response);
    }
  })
  console.log(data);*/

  Papa.parse("temp_map111.csv", {
    download: true,
    complete: function(result) {
      $('.map-area path').each(function(){
        let idPath = $(this).attr('id');
        //$(this).attr('data-amos', )
        $(this).attr('data-amos', result.data[idPath][0]);
        $(this).attr('data-begl', result.data[idPath][1]);
        $(this).attr('data-tih', result.data[idPath][2]);
        $(this).attr('data-okrug', result.data[idPath][3]);

        if (parseInt(result.data[idPath][0]) > parseInt(result.data[idPath][1]) && parseInt(result.data[idPath][0]) > parseInt(result.data[idPath][2])){
          $(this).addClass('green');
        } else if (parseInt(result.data[idPath][1]) > parseInt(result.data[idPath][0]) && parseInt(result.data[idPath][1]) > parseInt(result.data[idPath][2])){
          $(this).addClass('blue');
        } else {
          $(this).addClass('red');
        }
      })
    }
  });



  $(document).on('mouseover', '.map-area path', function(){
    var idPath = $(this).attr('id');
    $('.h1-okrug span').html($(this).data('okrug'));
    $('#h2-amos span').html($(this).data('amos'));
    $('#h2-begl span').html($(this).data('begl'));
    $('#h2-tih span').html($(this).data('tih'));
  })

  //console.log(results.data);



  /*
  var results = Papa.parse(csv, {
      header: true
  });
*/
})