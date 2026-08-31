"use strict";

const output = document.getElementById("rubaiyatOutput");
const status = document.getElementById("readerStatus");
const randomButton = document.getElementById("randomRubaiyat");
const boozeismButton = document.getElementById("randomRubaiyatInBoozeism");

let poems = [];
let boozeismPoems = [];

function pickRandom(candidates) {
  return candidates[Math.floor(Math.random() * candidates.length)];
}

function createParagraph(className, text) {
  const paragraph = document.createElement("p");
  paragraph.className = className;
  paragraph.textContent = text;
  return paragraph;
}

function renderPoem(poem) {
  const fragment = document.createDocumentFragment();
  fragment.append(
    createParagraph("poem-section", poem.section),
    createParagraph("poem-body", poem.poem_body),
    createParagraph("poem-number", `第${poem.id}歌`),
  );

  if (poem.footnote) {
    const footnote = document.createElement("aside");
    footnote.className = "footnote";
    footnote.setAttribute("aria-label", "脚注");
    footnote.append(createParagraph("footnote-text", poem.footnote));
    fragment.append(footnote);
  }

  output.replaceChildren(fragment);
  output.setAttribute("aria-busy", "false");
}

function showRandomPoem(candidates) {
  renderPoem(pickRandom(candidates));
}

function enableReader() {
  status.textContent = "上のボタンから、今の一首をひらいてください。";
  output.setAttribute("aria-busy", "false");
  randomButton.disabled = false;
  boozeismButton.disabled = false;
}

function showLoadError(error) {
  console.error("Failed to load Rubaiyat data:", error);
  status.textContent =
    "詩集を読み込めませんでした。時間をおいて、ページを再読み込みしてください。";
  output.classList.add("poem-card-error");
  output.setAttribute("aria-busy", "false");
}

function validateData(data) {
  if (!Array.isArray(data) || data.length === 0) {
    throw new Error("The poem collection is empty or invalid.");
  }

  const boozeism = data.filter((poem) => poem.is_boozeism === true);
  if (boozeism.length === 0) {
    throw new Error("The booze-ism collection is empty.");
  }

  return boozeism;
}

async function initialize() {
  try {
    const response = await fetch("data/rubaiyat.json");
    if (!response.ok) {
      throw new Error(`Data request failed with status ${response.status}.`);
    }

    poems = await response.json();
    boozeismPoems = validateData(poems);
    enableReader();
  } catch (error) {
    showLoadError(error);
  }
}

randomButton.addEventListener("click", () => showRandomPoem(poems));
boozeismButton.addEventListener("click", () => showRandomPoem(boozeismPoems));

initialize();
