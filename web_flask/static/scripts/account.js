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
    });

    delivery.addEventListener('click', function () {
      create_panel.style.display = 'none';
      profile_panel.style.display = 'none';
      history_panel.style.display = 'none';
      delivery_panel.style.display = 'block';
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
    });
    contact.addEventListener('click', function () {
      // Clear content in profile_panel
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
      console.log('Name:', name);
      console.log('Address:', address);
      console.log('phone number:', phoneNumber);
      console.log('city:', city);
      console.log('tracking:', tracking);
      console.log('sender name:', username.textContent);
      console.log('sender phone:', user_phone.textContent);
      console.log('sender city:', user_city.textContent);
  
      const wrapperDiv = document.createElement('div');
      wrapperDiv.innerHTML = '<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Download HTML Example</title> </head> <style> body { width: 40rem; } .container { background-color: white; background-image: none; } .cont{ border: solid; width: 100%; box-sizing: border-box; } .sender { margin: 2rem; display: flex; height: 7rem; border-bottom: 1px solid; } .sender_details{ display: flex; flex-direction: column; margin-left: 2rem; } h2 { margin: 0px; } h3 { margin: 0px 0 5px 0; } .reciever { margin: 2rem; display: flex; border-bottom: 1px solid; } .reciever_details{ display: flex; flex-direction: column; margin-left: 2rem; } .tracking { display: flex; margin-left: 2rem; margin-right: 2rem; /* justify-content: space-around; */ align-items: center; border-bottom: 1px solid; } .num { align-self: flex-start; margin-right: 4rem; } h1 { margin-right: 3rem; } div.logos { background-image: url("/static/img/shipit.jpg"); width: 250px; height: 100px; display: inline-block; background-position: center; margin-left: 13rem; margin-top: 3rem; border: none; } </style> <body> <div class="cont"> <div class="sender"> <h2>Sender:</h2> <div class="sender_details"> <h3>' + username.textContent + '</h3> <h3>' + user_city.textContent + '</h3> <h3>' + user_phone.textContent + '</h3> </div> </div> <div class="reciever"> <h2>Reciever</h2> <div class="reciever_details"> <h3>' + name + '</h3> <h3>' + phoneNumber + '</h3> <h3>' + address + '</h3> <h3>' + city + '</h3> <h3>' + postalcode + '</h3> </div> </div> <div class="tracking"> <h1 class="num">Tracking number</h1> <h1>' + tracking + '</h1> </div> <div class="logos"> </div> </div> </body> </html> '

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