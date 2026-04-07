const STORAGE_PREFIX = "repaso_examen_checklist_1min:";

function escapeHtml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function itemKey(topicId, itemId) {
  return `${STORAGE_PREFIX}${topicId}:${itemId}`;
}

function readMark(topicId, itemId) {
  return localStorage.getItem(itemKey(topicId, itemId)) || "";
}

function saveMark(topicId, itemId, value) {
  localStorage.setItem(itemKey(topicId, itemId), value);
}

function clearTopic(topic) {
  topic.items.forEach((item) => localStorage.removeItem(itemKey(topic.id, item.id)));
}

function renderCounts(topic, container) {
  const counts = {
    clear: 0,
    doubt: 0,
    no: 0,
    empty: 0,
  };

  topic.items.forEach((item) => {
    const value = readMark(topic.id, item.id);
    if (value === "clear") counts.clear += 1;
    else if (value === "doubt") counts.doubt += 1;
    else if (value === "no") counts.no += 1;
    else counts.empty += 1;
  });

  container.textContent =
    `Sin mirar: ${counts.clear} | Con dudas: ${counts.doubt} | No lo saco: ${counts.no} | Sin marcar: ${counts.empty}`;
}

function renderTopic(topic) {
  const section = document.createElement("section");
  section.className = "topic";
  section.id = topic.id;

  section.innerHTML = `
    <div class="topic-header">
      <div>
        <h2>${escapeHtml(topic.block_id)} - ${escapeHtml(topic.name)}</h2>
        <p>Haz solo estas 3 anclas. Si una no sale, vuelve al bloque de repaso. No hay nota ni veredicto del sistema.</p>
      </div>
      <a class="summary-link" href="${topic.summary_path}">Abrir repaso del tema</a>
    </div>
    <div class="items"></div>
    <div class="topic-footer">
      <div class="counts" data-role="counts"></div>
      <button class="reset-button" type="button">Borrar marcas del tema</button>
    </div>
  `;

  const itemsRoot = section.querySelector(".items");
  const counts = section.querySelector("[data-role='counts']");
  const resetButton = section.querySelector(".reset-button");

  topic.items.forEach((item, index) => {
    const article = document.createElement("article");
    article.className = "item";
    const currentValue = readMark(topic.id, item.id);
    article.innerHTML = `
      <span class="eyebrow">${index + 1}. ${escapeHtml(item.type)}</span>
      <h3>${escapeHtml(item.title)}</h3>
      <div class="prompt">${item.prompt_html}</div>
      <details>
        <summary>Mostrar solucion</summary>
        <div class="expected">${item.expected_html}</div>
      </details>
      <div class="self-check">
        <label><input type="radio" name="${item.id}" value="clear" ${currentValue === "clear" ? "checked" : ""}> Lo hago sin mirar</label>
        <label><input type="radio" name="${item.id}" value="doubt" ${currentValue === "doubt" ? "checked" : ""}> Lo saco con dudas</label>
        <label><input type="radio" name="${item.id}" value="no" ${currentValue === "no" ? "checked" : ""}> No lo saco</label>
      </div>
    `;

    article.querySelectorAll("input[type='radio']").forEach((input) => {
      input.addEventListener("change", () => {
        saveMark(topic.id, item.id, input.value);
        renderCounts(topic, counts);
      });
    });

    itemsRoot.appendChild(article);
  });

  resetButton.addEventListener("click", () => {
    clearTopic(topic);
    section.querySelectorAll("input[type='radio']").forEach((input) => {
      input.checked = false;
    });
    renderCounts(topic, counts);
  });

  renderCounts(topic, counts);
  return section;
}

async function main() {
  const response = await fetch("./data/topics.json");
  const data = await response.json();

  document.title = data.title;
  document.querySelector("[data-role='page-title']").textContent = data.title;

  const nav = document.querySelector("[data-role='topic-nav']");
  const content = document.querySelector("[data-role='topic-content']");

  data.topics.forEach((topic) => {
    const link = document.createElement("a");
    link.href = `#${topic.id}`;
    link.textContent = `${topic.block_id} - ${topic.name}`;
    nav.appendChild(link);
    content.appendChild(renderTopic(topic));
  });
}

main().catch((error) => {
  const root = document.querySelector("[data-role='topic-content']");
  root.innerHTML = `<p>No se ha podido cargar la checklist: ${escapeHtml(String(error))}</p>`;
});
