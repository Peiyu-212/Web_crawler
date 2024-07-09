
document.addEventListener('DOMContentLoaded', function() {
	const socket = new WebSocket('ws://'
		+ window.location.host
		+ '/ws/news/'
	);

	socket.onmessage = function(event) {
		const data = JSON.parse(event.data);
		if (data.text === 'New data available') {
			showToast(data.text);
		}
	};

	socket.onerror = function(error) {
		console.error('WebSocket Error: ', error);
	};

	socket.onclose = function() {
		console.log('WebSocket connection closed');
	};
});

const showToast = (message) => {
	const toastHTML = `
		<div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
			<div class="toast-header">
				<strong class="me-auto">Notification</strong>
				<small>Just now</small>
				<button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
			</div>
			<div class="toast-body">
				${message}<br />
				<button id="actionButton" class="btn btn-primary mt-2">Reload</button>
			</div>
		</div>`;

	const toastContainer = document.getElementById('toastContainer');
	const toastElement = document.createElement('div');
	toastElement.innerHTML = toastHTML;

	toastContainer.appendChild(toastElement.firstElementChild);

	$(".toast").show();

	document.getElementById('actionButton').addEventListener('click', function() {
		window.location.reload();
		toastElement.classList.remove('visible');
		setTimeout(function() {
				toastContainer.removeChild(toastElement);
		}, 5);
	});

};
