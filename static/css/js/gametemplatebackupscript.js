document.addEventListener('DOMContentLoaded', () => {
    const slider = document.getElementById('slider');
    const popup = document.getElementById('popup');
    const fire = popup.querySelector('.fire');
    const textContainer = popup.querySelector('.text');
    const persistSpinCheckbox = document.getElementById('persist-spin-checkbox');
    const quickSpinCheckbox = document.getElementById('quickspin-checkbox');
    const startButton = document.getElementById('start');

    let animationStopped = false;
    let selectedItems = [];
    let totalSpins = 1;
    let currentSpin = 0;

    const persistSpin = localStorage.getItem('persistSpinChecked') === 'true';
    const quickSpin = localStorage.getItem('quickSpinChecked') === 'true';

    // Initialize checkboxes from localStorage
    persistSpinCheckbox.checked = persistSpin;
    quickSpinCheckbox.checked = quickSpin;

    // Persist settings on checkbox change
    persistSpinCheckbox.addEventListener('change', () => {
        localStorage.setItem('persistSpinChecked', persistSpinCheckbox.checked.toString());
    });

    quickSpinCheckbox.addEventListener('change', () => {
        localStorage.setItem('quickSpinChecked', quickSpinCheckbox.checked.toString());
    });

    // Update total spins when a spin option is clicked
    document.querySelectorAll('.spin-option').forEach(option => {
        option.addEventListener('click', () => {
            document.querySelectorAll('.spin-option').forEach(opt => opt.classList.remove('selected'));
            option.classList.add('selected');
            totalSpins = parseInt(option.dataset.value);
            sessionStorage.setItem('totalSpins', totalSpins);
        });
    });

    // Start animation on button click
    startButton.addEventListener('click', () => {
        sessionStorage.setItem('startAnimation', 'true');
        sessionStorage.setItem('isQuickSpin', quickSpinCheckbox.checked);

        // Reset current spin count and initialize the animation
        currentSpin = 0;
        initializeAnimation();
    });

async function randomizeContents() {
    const gameId = startButton.getAttribute('data-game-id');
    const slug = startButton.getAttribute('data-slug');

    console.log("Game ID:", gameId);
    console.log("Slug:", slug);

    try {
        const payload = { game_id: gameId };
        console.log("Payload sent to server:", payload);

        const response = await fetch(`/create_outcome/${slug}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}', // Ensure CSRF token is included
            },
            body: JSON.stringify(payload),
        });

        const data = await response.json();
        console.log("Response from server:", data);

        if (data.status === 'success') {
            startButton.setAttribute('data-nonce', data.nonce);
            console.log(`Nonce updated: ${data.nonce}`);
            return data; // Return the entire data object
        } else {
            console.error(`Error: ${data.message}`);
            return null;
        }
    } catch (error) {
        console.error(`Request failed: ${error}`);
        return null;
    }
}


    function initializeAnimation() {
        startButton.disabled = true;
        const isQuickSpin = sessionStorage.getItem('isQuickSpin') === 'true';
        selectedItems = [];

        spin(isQuickSpin);
        console.log('spin called here')
    }

function alignCardToSelector(card) {
    const slider = document.getElementById('slider');
    const sliderWidth = slider.offsetWidth; // Width of the slider container
    const cardWidth = card.offsetWidth; // Width of the card
    const cardPosition = card.offsetLeft; // Card's position relative to the slider

    // Calculate the target scroll position to center the card
    const targetPosition = cardPosition - (sliderWidth / 2) + (cardWidth / 2);
    console.log('targetPosition: ' + targetPosition)
    // Smoothly scroll the slider to the target position
    slider.scrollTo({
        left: targetPosition,
        behavior: 'smooth',
    });
    console.log('location set successfully ')
}


function insertCardAtVisiblePosition(slider, targetCardElement) {
    const sliderWidth = slider.offsetWidth; // Width of the slider container
    const cardWidth = targetCardElement.offsetWidth || 100; // Default card width if not rendered yet
    const visibleMiddle = sliderWidth / 2; // Middle of the slider container

    // Calculate the total offset for the new card
    const cards = slider.querySelectorAll('.card');
    const currentScroll = slider.scrollLeft;
    const totalOffset = visibleMiddle + currentScroll - (cardWidth / 2);

    // Find the approximate position for insertion
    let insertBeforeCard = null;
    cards.forEach(card => {
        if (card.offsetLeft > totalOffset) {
            insertBeforeCard = card;
        }
    });

    // Insert the card before the found card or at the end if no card is found
    if (insertBeforeCard) {
        slider.insertBefore(targetCardElement, insertBeforeCard);
    } else {
        slider.appendChild(targetCardElement);
    }
}


async function spin(isQuickSpin) {
    $(".spin-option").prop('disabled', true);

    const data = await randomizeContents();
    if (!data) return;

    addAnimation(isQuickSpin);

    const animationDuration = isQuickSpin ? 4500 : 9000;
    const buffer = 150; // Buffer for timing
    const audio = new Audio('/static/css/sounds/roulette_sound_effect.mp3');
    audio.play().catch(error => console.error('Error playing audio:', error));

    const cards = document.querySelectorAll('#slider .card');
    let targetCard = null;

    // Check if the card exists
    cards.forEach(card => {
        if (card.getAttribute('data-nonce') === String(data.nonce)) {
            targetCard = card;
        }
    });

    const slider = document.getElementById('slider');

    // If the target card doesn't exist, create it
    if (!targetCard) {
        const attributes = {
            id: data.choice_id,
            nonce: data.nonce,
            text: data.choice_text,
            color: data.choice_color,
            file: data.choice_file,
        };

        const targetCardElement = document.createElement('div');
        targetCardElement.classList.add('card');
        targetCardElement.setAttribute('id', `card-${attributes.id}`);
        targetCardElement.setAttribute('data-nonce', attributes.nonce);
        targetCardElement.setAttribute('data-color', attributes.color);

        targetCardElement.innerHTML = `
            <div class="card-content" style="background-color: ${attributes.color}">
                <p>Nonce: ${attributes.nonce}</p>
                <p>${attributes.text}</p>
                ${attributes.file ? `<img src="${attributes.file}" alt="${attributes.text}">` : ''}
            </div>
        `;

        // Insert card in a visible position
        insertCardAtVisiblePosition(slider, targetCardElement);
        targetCard = targetCardElement; // Assign the newly created card as the target
    }

    // Stop animation after aligning the card
    setTimeout(() => {
        document.querySelectorAll('.slider').forEach(scroller => {
            scroller.style.animation = 'none'; // Stop the animation
        });

        alignCardToSelector(targetCard);

        // Increment current spin count
        currentSpin++;

        // Stop after reaching total spins
        if (currentSpin >= totalSpins) {
            animationStopped = true;

            // Show the popup with the result
            findSelectedCard(); // Add the selected card to selectedItems

            showPopup();

            if (!persistSpin) {
                totalSpins = 1; // Reset total spins if persist spin is disabled
                sessionStorage.setItem("totalSpins", totalSpins);
            }

            startButton.disabled = false; // Re-enable the start button
        }
    }, animationDuration + buffer); // Wait for animation to complete
}




    function addAnimation(isQuickSpin) {
        document.querySelectorAll('.slider').forEach(scroller => {
            scroller.style.animation = 'none';
            scroller.offsetHeight; // Trigger reflow
            let animationDuration = isQuickSpin ? '9s' : '18s';
            scroller.style.animation = `slideshow ${animationDuration} cubic-bezier(0.25, 0.1, 0.25, 1) forwards`;
            scroller.style.animationPlayState = 'running';
        });
    }


function findSelectedCard() {
    const selector = document.getElementById('selector').getBoundingClientRect();
    let currentSelection = null;

    document.querySelectorAll('.card').forEach(card => {
        const cardRect = card.getBoundingClientRect();
        if (
            !(selector.right < cardRect.left ||
              selector.left > cardRect.right ||
              selector.bottom < cardRect.top ||
              selector.top > cardRect.bottom)
        ) {
            currentSelection = {
                id: card.id,
                src: card.querySelector('img') ? card.querySelector('img').src : '',
                price: card.dataset.price || '0',
                color: card.dataset.color || '',
                value: card.dataset.value || 'N/A',
            };
        }
    });

    if (currentSelection) {
        selectedItems.push(currentSelection); // Add the card to the array
    }
}


function showPopup() {
    textContainer.innerHTML = `
        <h2>Congratulations!</h2>
        <p>You got:</p>
        <div class="cards-container"></div>
        <button class="close">Collect</button>
    `;

    const cardsContainer = textContainer.querySelector('.cards-container');
    selectedItems.forEach(item => {
        const cardElement = document.createElement('div');
        cardElement.classList.add('popup-card');
        cardElement.innerHTML = `
            <div class="card-fire" data-color="${item.color}">
                <div class="card-flames">
                    <div class="card-flame"></div>
                </div>
            </div>
            <p>ID: ${item.id}</p>
            <img src="${item.src}" alt="${item.id}">
            <p>Price: $${item.price}</p>
            <p>Value: ${item.value}</p>
        `;
        cardsContainer.appendChild(cardElement);
    });

    popup.style.display = 'block';
    fire.classList.add('active');

    popup.querySelector('.close').addEventListener('click', () => {
        fire.classList.remove('active');
        popup.style.display = 'none';
    });
}
});












