// Lightbox configuration for Ganadera website
document.addEventListener('DOMContentLoaded', function() {
    // Configure lightbox options
    lightbox.option({
        'resizeDuration': 200,
        'wrapAround': true,
        'albumLabel': 'Imagen %1 de %2',
        'fadeDuration': 300,
        'imageFadeDuration': 300,
        'positionFromTop': 50,
        'showImageNumberLabel': true,
        'alwaysShowNavOnTouchDevices': true,
        'enableKeyboardNav': true,
        'disableScrolling': true,
        'fitImagesInViewport': true,
        'maxWidth': 1200,
        'maxHeight': 800,
        'minWidth': 200,
        'minHeight': 200,
        'onOpen': function() {
            // Add custom class to body when lightbox is open
            document.body.classList.add('lightbox-open');
        },
        'onClose': function() {
            // Remove custom class when lightbox is closed
            document.body.classList.remove('lightbox-open');
        }
    });

    // Prevent default behavior for lightbox links
    document.addEventListener('click', function(e) {
        if (e.target.closest('a[data-lightbox]')) {
            e.preventDefault();
        }
    });

    // Custom lightbox events
    lightbox.option({
        'onOpen': function() {
            // Add custom class to body when lightbox is open
            document.body.classList.add('lightbox-open');
        },
        'onClose': function() {
            // Remove custom class when lightbox is closed
            document.body.classList.remove('lightbox-open');
        }
    });

    // Add custom styles for lightbox
    const style = document.createElement('style');
    style.textContent = `
        .lightbox-open {
            overflow: hidden;
        }
        
        .lb-outerContainer {
            border-radius: 8px;
        }
        
        .lb-dataContainer {
            border-radius: 0 0 8px 8px;
        }
        
        .lb-nav a.lb-prev,
        .lb-nav a.lb-next {
            opacity: 0.8;
        }
        
        .lb-nav a.lb-prev:hover,
        .lb-nav a.lb-next:hover {
            opacity: 1;
        }
        
        .lb-number {
            font-family: 'Inter', sans-serif;
            font-size: 14px;
        }
        
        .lb-data .lb-caption {
            font-family: 'Inter', sans-serif;
            font-size: 16px;
            font-weight: 500;
        }
        
        .lb-closeContainer {
            padding: 10px;
        }
        
        .lb-close {
            opacity: 0.8;
        }
        
        .lb-close:hover {
            opacity: 1;
        }
    `;
    document.head.appendChild(style);
}); 