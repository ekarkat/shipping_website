document.addEventListener('DOMContentLoaded', function () {
    const profile_panel = document.querySelector('.profile_panel');
    const create_panel = document.querySelector('.create_panel');
    const history_panel = document.querySelector('.history_panel');	
    const delivery_panel = document.querySelector('.delivery_panel');
    const contactus_panel = document.querySelector('.contactus_panel');
    const people = document.querySelector('.people');
    const create = document.querySelector('.create');
    const history = document.querySelector('.history');
    const delivery = document.querySelector('.delivery');
    const contact = document.querySelector('.contact');


	$(document).ready(function() {
		var stateId = ''; // Initialize stateId variable
	
		$('#states').change(function() {
			stateId = $(this).val();
			getCities(stateId);
		});

	
		function getCities(stateId) {
			// Make AJAX request to retrieve cities
			$.ajax({
				url: 'http://localhost:5600/api/v1/states/cities/' + stateId,
				type: 'GET',
				success: function(data) {
					// Clear existing options in cities dropdown
					$('#cities').empty();
					// Add new options for cities
					$.each(data, function(index, city) {
						$('#cities').append($('<option>', {
							value: city.id,
							text: city.name
						}));
					});
				},
				error: function(xhr, status, error) {
					// Handle error
					console.error(error);
				}
			});
		}
	});

  
    // Variables to store content
    let profilePanelContent = profile_panel.innerHTML;
    let createPanelContent = create_panel.innerHTML;
    let contactusPanelContent = contactus_panel.innerHTML;


	createPanelContent = create_panel.innerHTML;
	create_panel.innerHTML = '';
	contactusPanelContent = contactus_panel.innerHTML;
	contactus_panel.innerHTML = '';


    history.addEventListener('click', function () {
      create_panel.style.display = 'none';
      profile_panel.style.display = 'none';
      delivery_panel.style.display = 'none';
      history_panel.style.display = 'block';
	  contactus_panel.style.display = 'none';
    });

    delivery.addEventListener('click', function () {
      create_panel.style.display = 'none';
      profile_panel.style.display = 'none';
      history_panel.style.display = 'none';
      delivery_panel.style.display = 'block';
	  contactus_panel.style.display = 'none';
    });

    people.addEventListener('click', function () {
		// Clear content in create_panel



		if (create_panel.innerHTML === '') {
		}
		else {
			createPanelContent = create_panel.innerHTML;
			create_panel.innerHTML = '';
		}
		if (contactus_panel.innerHTML === '') {
		}
		else {
			contactusPanelContent = contactus_panel.innerHTML;
			contactus_panel.innerHTML = '';
		}

		profile_panel.innerHTML = profilePanelContent;
		create_panel.style.display = 'none';
		profile_panel.style.display = 'flex';
		history_panel.style.display = 'none';
		delivery_panel.style.display = 'none';
		contactus_panel.style.display = 'none';

	  stateId = '';
	  		$('#states').change(function() {
			stateId = $(this).val();
			getCities(stateId);
		});
		function getCities(stateId) {
			// Make AJAX request to retrieve cities
			$.ajax({
				url: 'http://localhost:5600/api/v1/states/cities/' + stateId,
				type: 'GET',
				success: function(data) {
					// Clear existing options in cities dropdown
					$('#cities').innerHTML="";
					$('#cities').empty();
					// Add new options for cities
					$.each(data, function(index, city) {
						$('#cities').append($('<option>', {
							value: city.id,
							text: city.name
						}));
					});
				},
				error: function(xhr, status, error) {
					// Handle error
					console.error(error);
				}
			});
		}
		$("#panel_number").val(1);
    });
  
    create.addEventListener('click', function () {
	// Clear content in profile_panel

	if (profile_panel.innerHTML === '') {
	}
	else {
		profilePanelContent = profile_panel.innerHTML;
		profile_panel.innerHTML = '';
	}
			if (contactus_panel.innerHTML === '') {
	}
	else {
		contactusPanelContent = contactus_panel.innerHTML;
		contactus_panel.innerHTML = '';
	}
	create_panel.innerHTML = createPanelContent;
	profile_panel.style.display = 'none';
	create_panel.style.display = 'flex';
	history_panel.style.display = 'none';
	delivery_panel.style.display = 'none';
	contactus_panel.style.display = 'none';

	var c_stateId = ''; // Initialize stateId variable
	$('#create_states').change(function() {
		c_stateId = $(this).val();
		getCities(c_stateId, function() {
			// Callback function to be executed after cities are retrieved and dropdown is populated
			var userCityn = $('.user_cit').text();
			const firstOption = document.querySelector('#create_cities option:first-child');
			var selectedCityn = firstOption.textContent;
			console.log("Selected City:", selectedCityn);
			console.log("User's City:", userCityn);
			// Call getDistance with a callback function to handle the result
			getDistance(userCityn, selectedCityn, function(distance) {
				updatePrice(distance);
			});
		});
	});
	
	function getCities(c_stateId, callback) {
		// Make AJAX request to retrieve cities
		$.ajax({
			url: 'http://localhost:5600/api/v1/states/cities/' + c_stateId,
			type: 'GET',
			success: function(data) {
				// Clear existing options in cities dropdown
				$('#create_cities').empty();
				// Add new options for cities
				$.each(data, function(index, city) {
					$('#create_cities').append($('<option>', {
						value: city.id,
						text: city.name
					}));
				});
				// Call the callback function to indicate that cities have been populated
				callback();
			},
			error: function(xhr, status, error) {
				// Handle error
				console.error(error);
			}
		});
	}

		// Function to retrieve distance between two cities using Google Maps Distance Matrix API
		function getDistance(origin, destination, callback) {
			const apiUrl = `http://localhost/dist/${origin}-${destination}`;
			$.ajax({
				url: apiUrl,
				type: 'GET',
				success: function(data) {
					const distance = data['distance'];
					console.log(distance);
					callback(distance);
				},
				error: function(xhr, status, error) {
					console.error(error);
					callback(null);
				}
			});
		}

		// Function to calculate price based on distance
		function calculatePrice(distance) {
			if (distance < 100) {
				return 15;
			} else if (distance < 250) {
				return 20;
			} else if (distance < 500) {
				return 30;
			} else if (distance < 650) {
				return 35;
			} else if (distance < 850) {
				return 40;
			} else {
				return 45;
			}
		}

		// Initialize a variable to store the initial price
		var initialPrice = parseFloat($('.price').text());
		// Function to update price element
		function updatePrice(distance) {
			const priceElement = $('.price');
			const costElement = $('#parcel_cost');
			var selectedValue = $('#parcel_type').val();
			if (distance !== null) {
				const price = calculatePrice(distance);
				priceElement.text(price + ' MAD');
				costElement.val(price);
				initialPrice = price
				if (selectedValue === "express") {
					// Calculate the price only the first time express is selected
					var expressPrice = initialPrice * 1.75;
					priceElement.text(expressPrice + ' MAD');
					costElement.val(expressPrice);
				} else if (selectedValue === "standard") {
					// Set the price back to the initial value for standard
					priceElement.text(initialPrice + ' MAD');
					costElement.val(initialPrice);
				}

			} else {
				priceElement.text('Error occurred while calculating price.');
			}
		}

		// print the selected city in the console.log
		$('#create_cities').change(function() {
			var userCity = $('.user_cit').text();
			var selectedCity = $(this).find(":selected").text();
			console.log("Selected City:", selectedCity);
			console.log("User's City:", userCity);
			// Call getDistance with a callback function to handle the result
			getDistance(userCity, selectedCity, function(distance) {
				updatePrice(distance);
			});
		});


		var alreadySelectedValue = $('#parcel_type').val();

		// Add event listener for change event on the parcel_type select element
		$('#parcel_type').change(function() {
			// Get the value of the selected option
			var selectedValue = $(this).val();
			const priceElement = $('.price');
			const costElement = $('#parcel_cost');
		
			// Check the selected value
			if (selectedValue === "express") {
				// Calculate the price only the first time express is selected
				if (alreadySelectedValue === "express"){
					priceElement.text(initialPrice + ' MAD');
					costElement.val(initialPrice);
				}
				else {
					var expressPrice = initialPrice * 1.75;
					priceElement.text(expressPrice + ' MAD');
					costElement.val(expressPrice);
				}

			} else if (selectedValue === "standard") {
				// Set the price back to the initial value for standard
				if (alreadySelectedValue === "standard"){
					priceElement.text(initialPrice + ' MAD');
					costElement.val(initialPrice);
				}
				else {
					var expressPrice = initialPrice / 1.75;
					priceElement.text(expressPrice + ' MAD');
					costElement.val(expressPrice);
				}
			}
		});
		$("#panel_number").val(2);
    });

    contact.addEventListener('click', function () {
      // Clear content in profile_panel
	  panel_3.value = "3";
      if (profile_panel.innerHTML === '') {
      }
      else {
        profilePanelContent = profile_panel.innerHTML;
        profile_panel.innerHTML = '';
      }
      if (create_panel.innerHTML === '') {
      }
      else {
        createPanelContent = create_panel.innerHTML;
        create_panel.innerHTML = '';
      }
      contactus_panel.innerHTML = contactusPanelContent;
      profile_panel.style.display = 'none';
      create_panel.style.display = 'none';
      history_panel.style.display = 'none';
      delivery_panel.style.display = 'none';
      contactus_panel.style.display = 'flex';
    });

	var panel_num = document.querySelector('.panel_num_fix').textContent;

	// Print the content to the console
	console.log(panel_num);

	if (panel_num === "1")
		people.click()
	if (panel_num === "2")
		create.click()
	if (panel_num === "3")
		contact.click()
  });

//  print function

  $(document).ready(function () {
    // Add click event listener to elements with class "print"
    $('.print').on('click', function () {
      // Get the data from the other <td> elements in the same row
      var name = $(this).closest('tr').find('td:eq(3)').text(); // Index 3 corresponds to the "to_name" column
      var address = $(this).closest('tr').find('td:eq(5)').text(); // Index 5 corresponds to the "to_address" column
      var phoneNumber = $(this).closest('tr').find('td:eq(4)').text(); // Index 5 corresponds to the "to_address" column
      var city = $(this).closest('tr').find('td:eq(2)').text(); // Index 5 corresponds to the "to_address" column
      var postalcode = $(this).closest('tr').find('td:eq(6)').text(); // Index 5 corresponds to the "to_address" column
      var tracking = $(this).closest('tr').find('td:eq(0)').text(); // Index 5 corresponds to the "to_address" column
      var username = document.querySelector('.user_name');
      var user_phone = document.querySelector('.user_phone');
      var user_city = document.querySelector('.user_city');
  
      // Now you can use 'name' and 'address' as needed

  
      const wrapperDiv = document.createElement('div');
      wrapperDiv.innerHTML = '<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Download HTML Example</title> </head> <style> body { width: 35rem; } .container { background-color: white; background-image: none; } .cont{ border: solid; width: 90%; box-sizing: border-box; } .sender { margin: 2rem; display: flex; height: 7rem; border-bottom: 1px solid; } .sender_details{ display: flex; flex-direction: column; margin-left: 2rem; } h2 { margin: 0px; } h3 { margin: 0px 0 5px 0; } .reciever { margin: 2rem; display: flex; border-bottom: 1px solid; } .reciever_details{ display: flex; flex-direction: column; margin-left: 2rem; } .tracking { display: flex; margin-left: 2rem; margin-right: 2rem; /* justify-content: space-around; */ align-items: center; border-bottom: 1px solid; } .num { align-self: flex-start; margin-right: 4rem; } h1 { margin-right: 3rem; } div.logos { background-image: url("/static/img/shipit.jpg"); width: 250px; height: 100px; display: inline-block; background-position: center; margin-left: 13rem; margin-top: 3rem; border: none; } </style> <body> <div class="cont"> <div class="sender"> <h2>Sender:</h2> <div class="sender_details"> <h3>' + username.textContent + '</h3> <h3>' + user_city.textContent + '</h3> <h3>' + user_phone.textContent + '</h3> </div> </div> <div class="reciever"> <h2>Reciever</h2> <div class="reciever_details"> <h3>' + name + '</h3> <h3>' + phoneNumber + '</h3> <h3>' + address + '</h3> <h3>' + city + '</h3> <h3>' + postalcode + '</h3> </div> </div> <div class="tracking"> <h1 class="num">Tracking number</h1> <h1>' + tracking + '</h1> </div> <div class="logos"> </div> </div> </body> </html> '

      // Create a new div to wrap the content you want to print
      const printContentDiv = document.createElement('div');
      printContentDiv.className = 'print-content';
      printContentDiv.innerHTML = wrapperDiv.innerHTML;

      // Use html2pdf to generate PDF and initiate download
      html2pdf(printContentDiv, {
        margin: 10,
        filename: 'parcel_label.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
      }).then(function (pdf) {
        // Trigger download
        pdf.save();
      });
    });
  });


  $(document).ready(function () {
    // Add click event listener to elements with class "delete"
    $('.delete').on('click', function () {
      // Get the parcel ID from the data attribute
      var parcelId = $(this).data('id');
      var currentRow = $(this).closest('tr');
      // Confirm deletion with the user (optional)
      if (confirm('Are you sure you want to delete this parcel?')) {
        // Send a simple request to your own backend
        fetch(`http://localhost:5600/api/v1/parcels/${parcelId}`, {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json',
            // You may need to include additional headers such as authorization headers
          },
        })
        .then(response => {
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          return response.json();
        })
        .then(data => {
          console.log('Parcel deleted successfully:', data);
          // You may want to update the UI or perform other actions after successful deletion
        }).then(data => {
            console.log('Parcel deleted successfully:', data);
            // Reload the page after successful deletion
            currentRow.remove();

        })
        .catch(error => {
          console.error('Error deleting parcel:', error);
          // Handle errors accordingly
        });
      }
    });
  });