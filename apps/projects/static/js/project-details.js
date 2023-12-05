// project-details.js
function showProjectDetails(name, summary, imageUrl, githubUrl, youtubeUrl) {
    var detailsHtml = `
        <div class="div-project-detail">
            <div class="project-image">
                <img src="${imageUrl}">
            </div>
            <div class="project-title d-flex text-center justify-content-center align-items-center">
                <h4>${name}</h4>
            </div>
        </div>
        <div class="div-project-detail">
            <div class="div-connected-links align-items-center">
                ${githubUrl ? `
                    <div class="div-link-to-source rounded-3 d-flex align-items-center">
                        <a href="${githubUrl}" target="_blank">
                            <img src="{% static '/images/github-logo.png' %}">
                        </a>
                    </div>
                ` : ''}
                ${youtubeUrl ? `
                    <div class="div-link-to-source rounded-3 d-flex align-items-center">
                        <a href="${youtubeUrl}" target="_blank">
                            <img src="{% static '/images/youtube-logo.png' %}">
                        </a>
                    </div>
                ` : ''}
            </div>
            <div class="div-project-detail-summary px-4">
                ${summary}
            </div>
        </div>
    `;
    document.getElementById('project-details').innerHTML = detailsHtml;
}
