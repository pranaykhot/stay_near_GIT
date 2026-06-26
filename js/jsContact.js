function getData() {
  // alert("Hi");
  var formData = new FormData();
  formData.append(
    "csrfmiddlewaretoken",
    $("input[name=csrfmiddlewaretoken]").val()
  );
  formData.append("action", "getData");

  $.ajax({
    url: "/get_contacts/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (response) {
      // console.log(response);
      for (let i = 0; i < response.length; i++) {
        let j = i + 1;

        $("#tableData").append(
          "<tr><td>" +
            j +
            '</td><td style="display: none;">' +
            response[i].ct_id +
            "</td><td>" +
            response[i].ct_name +
            "</td><td>" +
            response[i].ct_mobile +
            "</td><td>" +
            response[i].ct_email +
            "</td><td>" +
            response[i].ct_subject +
            "</td><td>" +
            response[i].ct_message +
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
