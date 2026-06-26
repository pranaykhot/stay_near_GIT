function getData() {
  // alert("Hi");
  var formData = new FormData();
  formData.append(
    "csrfmiddlewaretoken",
    $("input[name=csrfmiddlewaretoken]").val()
  );
  formData.append("action", "getData");

  $.ajax({
    url: "/get_bookings/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (response) {
      // console.log(response);
      for (var i = 0; i < response.length; i++) {
        var j = i + 1;
        // let image = response[i].ho_image.substring(3);

        $("#tableData").append(
          "<tr><td>" +
            j +
            '</td><td style="display: none;">' +
            response[i].or_id +
            "</td><td>" +
            response[i].or_name +
            "</td><td>" +
            response[i].or_total_amount +
            "</td><td>" +
            response[i].or_transaction_id +
            "</td><td>" +
            response[i].or_status +
            "</td></tr>"
        );
      }
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {},
  });
}

getData();
