function validateEmail(paramEmailID) {
  let filter = /^[0-9a-z.]+\@[a-z0-9]+\.[a-zA-z0-9]{2,4}$/;

  if (filter.test(paramEmailID)) {
    return true;
  } else {
    return false;
  }
}

function alphaOnly(event) {
  let key = event.which ? event.which : event.keyCode;
  return (
    (key >= 65 && key <= 90) ||
    key == 8 ||
    (event.charCode >= 97 && event.charCode <= 122) ||
    event.charCode == 32
  );
}

// alert("Hello");

$("#btn_add").click(function (e) {
  //verification
  if ($("#txtName").val().trim().length < 1) {
    alert("Please Enter Name");
    $("#txtName").focus();
    return false;
  }

  if ($("#txtPrice").val().trim().length < 1) {
    alert("Please Enter Rent / Month");
    $("#txtPrice").focus();
    return false;
  }

  if ($("#txtDetail").val().trim().length < 1) {
    alert("Please Enter Details");
    $("#txtDetail").focus();
    return false;
  }

  if ($("#txtAddress").val().trim().length < 1) {
    alert("Please Enter Details");
    $("#txtAddress").focus();
    return false;
  }

  if ($("#txtLocation").val().trim().length < 1) {
    alert("Please Enter Details");
    $("#txtLocation").focus();
    return false;
  }

  if ($("#txtImage").val() == "") {
    alert("Please choose Image");
    $("#txtImage").focus();
    return false;
  }

  // database
  let formData = new FormData();
  let lclFile = document.getElementById("txtImage");
  lclImage = lclFile.files[0];
  formData.append("txtName", $("#txtName").val());
  formData.append("txtPrice", $("#txtPrice").val());
  formData.append("txtDetail", $("#txtDetail").val());
  formData.append("txtAddress", $("#txtAddress").val());
  formData.append("txtLocation", $("#txtLocation").val());
  formData.append("txtImage", lclImage);
  formData.append(
    "csrfmiddlewaretoken",
    $("input[name=csrfmiddlewaretoken]").val()
  );
  formData.append("action", "add");

  $.ajax({
    beforeSend: function () {
      $(".btn .spinner-border").show();
      $("#btn_add").attr("disabled", true);
    },
    url: "/addPG/",
    type: "POST",
    // headers: {'X-CSRFToken': '{{ csrf_token }}'},
    data: formData,
    processData: false,
    contentType: false,
    success: function (result) {
      alert("Details Added Successfully");
      location.reload();
      table.ajax.reload();
      $("#add_modal").modal("hide");
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {
      $(".btn .spinner-border").hide();
      $("#btn_add").attr("disabled", false);
    },
  });
});
// data fetching (display into admin dashboard )
function getAdminData() {
  // alert("Hi");
  let formData = new FormData();
  formData.append(
    "csrfmiddlewaretoken",
    $("input[name=csrfmiddlewaretoken]").val()
  );
  formData.append("action", "getData");

  $.ajax({
    url: "/addPG/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (response) {
      console.log(response);
      // $("#dataTables-example tr:gt(0)").remove();
      for (var i = 0; i < response.length; i++) {
        var j = i + 1;
        let image = response[i].ab_image.substring(3);
        $("#tableData").append(
          "<tr><td>" +
            j +
            '</td><td style="display: none;">' +
            response[i].ab_id +
            "</td><td>" +
            response[i].ab_name +
            "</td><td>" +
            response[i].ab_price +
            "</td><td>" +
            response[i].ab_details +
            "</td><td>" +
            response[i].ab_address +
            '</td><td><a href="' +
            response[i].ab_location +
            '" target="_blank">Location</a></td><td><a href="' +
            image +
            '" download>download</a></td><td><div class="d-flex" style="justify-content: space-evenly;"><a href="javascript:void(0);" id="edit_row" title="View/Edit" data-toggle="modal" data-target="#edit_modal"  class="text-primary" onClick="getRowsUpdate();">Edit</a><a href="javascript:void(0);" title="Delete" data-toggle="modal" data-target="#delete_modal" class="text-danger" id="delete_row" onClick="getRowsDelete();">Delete</a></div></td></tr>'
        );
      }
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {},
  });
}

// Edit data
//Edit modal submit click
$(document).on("click", "#btn_update", function () {
  // alert("hi");

  if ($("#txtName1").val().trim().length < 1) {
    alert("Please Enter Name");
    $("#txtName1").focus();
    return false;
  }

  if ($("#txtPrice1").val().trim().length < 1) {
    alert("Please Enter Price");
    $("#txtPrice1").focus();
    return false;
  }

  if ($("#txtDetail1").val().trim().length < 1) {
    alert("Please Enter Detail");
    $("#txtDetail1").focus();
    return false;
  }

  if ($("#txtAddress1").val().trim().length < 1) {
    alert("Please Enter Address");
    $("#txtAddress1").focus();
    return false;
  }

  let formData = new FormData();
  formData.append("txtName1", $("#txtName1").val());
  formData.append("txtPrice1", $("#txtPrice1").val());
  formData.append("txtDetail1", $("#txtDetail1").val());
  formData.append("txtAddress1", $("#txtAddress1").val());
  formData.append("id", $("#edit_id").val());
  formData.append(
    "csrfmiddlewaretoken",
    $("input[name=csrfmiddlewaretoken]").val()
  );
  formData.append("action", "update");

  $.ajax({
    beforeSend: function () {
      $(".btn .spinner-border").show();
      $("#btn_update").attr("disabled", true);
    },
    url: "/addPG/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (result) {
      alert(" Details Updated Succesfully");
      location.reload();
      table.ajax.reload();
      $("#edit_modal").modal("hide");
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {
      $(".btn .spinner-border").hide();
      $("#btn_update").attr("disabled", false);
    },
  });
});

function getRowsUpdate() {
  $("#tableData tr").click(function () {
    let currentRow = $(this).closest("tr");
    let lclID = currentRow.find("td:eq(1)").text();
    let lclName = currentRow.find("td:eq(2)").text();
    let lclPrice = currentRow.find("td:eq(3)").text();
    let lclDetail = currentRow.find("td:eq(4)").text();
    let lclAddress = currentRow.find("td:eq(5)").text();
    // let lclLocation = currentRow.find("td:eq(6)").text();
    // alert(lclLocation);

    $("#txtName1").val(lclName);
    $("#txtPrice1").val(lclPrice);
    $("#txtDetail1").val(lclDetail);
    $("#txtAddress1").val(lclAddress);
    // $("#txtLocation1").val(lclLocation);
    $("#edit_id").val(lclID);
  });
}
// Delete
$(document).on("click", "#btn_delete", function () {
  // alert("hi");
  var formData = new FormData();
  formData.append("id", $("#delete_id").val());
  formData.append(
    "csrfmiddlewaretoken",
    $("input[name=csrfmiddlewaretoken]").val()
  );
  formData.append("action", "delete");

  // var table = $("#dataTables-example").DataTable();

  $.ajax({
    beforeSend: function () {
      $(".btn .spinner-border").show();
      $("#btn_update").attr("disabled", true);
    },
    url: "/addPG/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (result) {
      alert(" Details deleted Succesfully");
      location.reload();
      table.ajax.reload();
      $("#edit_modal").modal("hide");
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {
      $(".btn .spinner-border").hide();
      $("#btn_update").attr("disabled", false);
    },
  });
});

function getRowsDelete() {
  $("#tableData tr").click(function () {
    var currentRow = $(this).closest("tr");
    var lclID = currentRow.find("td:eq(1)").text();
    // alert(lclID);
    $("#delete_id").val(lclID);
  });
}
getAdminData();
