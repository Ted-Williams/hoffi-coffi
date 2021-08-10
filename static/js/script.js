onSelectCoffee = (event) => {
  const coffee = document.getElementById('edit-coffee').value;
  const selectedCoffee = JSON.parse(JSON.stringify(coffee));
  document.getElementsByName('coffeeName').value = selectedCoffee.product_name;
  console.log(selectedCoffee)
}

submitContactForm = () => {
  const successAlert = `
  <div class="alert alert-primary alert-dismissible" role="alert" id="contactSuccessAlert">
    Message successfully sent!
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  </div>
  `
  const failedAlert = `
  <div class="alert alert-danger alert-dismissible" role="alert" id="contactFailedAlert">
    Message failed to send. Please try again later.
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  </div>
  `

  const name = document.getElementById('user_name').value;
  const email = document.getElementById('user_email').value;
  const message = document.getElementById('message').value;

  if (name && email && message) {
    emailjs.sendForm('service_dh6n4z7', 'template_g4njnc7', '#contactForm').then((response) => {
      console.log('SUCCESS!', response.status, response.text);
      const contactAlert = document.getElementById('contactAlert')
      contactAlert.innerHTML = successAlert;
    }, (error) => {
      console.log('FAILED...', error);
      const contactAlert = document.getElementById('contactAlert')
      contactAlert.innerHTML = failedAlert;
    });
  } else {
    let missingFields = [];
    if (!name) missingFields.push('Name');
    if (!email) missingFields.push('Email');
    if (!message) missingFields.push('Message');

    const missingFieldsMessage = missingFields.join(' and ');
    const failedAlert = `
    <div class="alert alert-danger alert-dismissible" role="alert" id="contactFailedAlert">
      ${missingFieldsMessage} ${missingFields.length === 1 ? 'is a required field' : 'are required fields'}.
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    `
    const contactAlert = document.getElementById('contactAlert');
    contactAlert.innerHTML = failedAlert;
  }
}
