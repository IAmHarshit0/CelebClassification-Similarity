const fileInput = document.getElementById("fileInput");
const uploadIcon = document.getElementById("uploadIcon");
const uploadText = document.getElementById("uploadText");
const uploadSubText = document.getElementById("uploadSubText");

fileInput.addEventListener("change", () => {
  const file = fileInput.files[0];
  console.log(file);
  uploadIcon.innerHTML = `<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                                d="M5 13l4 4L19 7" />`;
  uploadIcon.classList.remove("text-gray-500");
  uploadIcon.classList.add("text-green-500");

  // Update text
  uploadText.textContent = "Image Uploaded Successfully!";
  uploadText.classList.remove("text-gray-500");
  uploadText.classList.add("text-green-600", "font-semibold");

  uploadSubText.textContent = file.name;
  uploadSubText.classList.remove("text-gray-400");
  uploadSubText.classList.add("text-gray-600");
});

const loadingIndicator = document.getElementById("loading");

async function uploadAndClassify() {
  const file = fileInput.files[0];
  if (!file) {
    alert("Please select an image first");
    return;
  }

  loadingIndicator.classList.remove("hidden");

  console.log("=== CLASSIFY DEBUG ===");
  console.log("File:", file);
  console.log("File name:", file.name);
  console.log("File type:", file.type);
  console.log("File size:", file.size);

  try {
    const formData = new FormData();
    formData.append("image", file);

    console.log("FormData created, sending request...");

    const response = await fetch("/classify", {
      method: "POST",
      body: formData,
    });

    console.log("Response status:", response.status);
    console.log("Response ok:", response.ok);
    console.log("Response headers:", response.headers);

    if (!response.ok) {
      const errorText = await response.text();
      console.log("Error response:", errorText);
      throw new Error(
        `HTTP error! status: ${response.status}, message: ${errorText}`
      );
    }

    const result = await response.json();
    console.log("Parsed JSON result:", result);

    const resultContainer = document.getElementById("result_container");
    console.log("Result container found:", resultContainer);

    if (!resultContainer) {
      console.error("ERROR: result_container element not found!");
      alert("Error: result_container element not found in HTML!");
      return;
    }

    resultContainer.classList.remove("hidden");
    resultContainer.innerHTML = `
    <div class="flex items-center justify-center m-2">
      <div class="p-4 bg-white rounded-lg shadow-md w-full max-w-md font-mono">
        <h2 class="text-xl font-bold mb-2 text-center text-green-600">Classification Result</h2>
        <p class="text-gray-700 text-center">${result.result || result}</p>
      </div>
    </div>
    `;
    console.log("Result displayed in container");
    document.getElementById("result_container").scrollIntoView({
      behavior: "smooth",
      block: "start",
    });
  } catch (error) {
    console.error("Error:", error);
    alert("Error classifying image: " + error.message);
  } finally {
    loadingIndicator.classList.add("hidden");
  }
}

document
  .querySelector(".classify-btn")
  .addEventListener("click", uploadAndClassify);

document
  .querySelector(".similarity-btn")
  .addEventListener("click", async () => {
    const file = fileInput.files[0];
    if (!file) return alert("Please select an image!");

    loadingIndicator.classList.remove("hidden");

    console.log("=== SIMILARITY DEBUG ===");
    console.log("File:", file);
    console.log("File name:", file.name);
    console.log("File type:", file.type);
    console.log("File size:", file.size);

    try {
      const formData = new FormData();
      formData.append("image", file);

      console.log("FormData created, sending request...");

      const response = await fetch("/similarity", {
        method: "POST",
        body: formData,
      });

      console.log("Response status:", response.status);
      console.log("Response ok:", response.ok);

      if (!response.ok) {
        const errorText = await response.text();
        console.log("Error response:", errorText);
        throw new Error(
          `HTTP error! status: ${response.status}, message: ${errorText}`
        );
      }

      const result = await response.json();
      console.log("Similarity result:", result);

      const resultContainer = document.getElementById("result_container");
      console.log("Result container found:", resultContainer);

      if (!resultContainer) {
        console.error("ERROR: result_container element not found!");
        alert("Error: result_container element not found in HTML!");
        return;
      }

      resultContainer.classList.remove("hidden");

      displaySimilarity(result);

      document.getElementById("result_container").scrollIntoView({
        behavior: "smooth",
        block: "start",
      });

      console.log("Similarity result displayed in container");
    } catch (error) {
      console.error("Error:", error);
      alert("Error getting similarity: " + error.message);
    } finally {
      loadingIndicator.classList.add("hidden");
    }
  });

function displaySimilarity(result) {
  const resultContainer = document.getElementById("result_container");
  resultContainer.classList.remove("hidden");

  const bestMatch = result.Best_Match;
  const bestCelebrity = result.Best_Celebrity;

  const menSection = result.Men.map((item) => {
    const [name, score] = Object.entries(item)[0];
    return `
      <div class="flex justify-between p-2 bg-gray-100 rounded-md">
        <span class="font-medium font-mono">${name.replaceAll("_", " ")}</span>
        <span class="${
          parseFloat(score) > 50 ? "text-green-600" : "text-gray-500"
        }">${score}</span>
      </div>
    `;
  }).join("");

  const womenSection = result.Women.map((item) => {
    const [name, score] = Object.entries(item)[0];
    return `
      <div class="flex justify-between p-2 bg-gray-100 rounded-md">
        <span class="font-medium font-mono">${name.replaceAll("_", " ")}</span>
        <span class="${
          parseFloat(score) > 50 ? "text-green-600" : "text-gray-500"
        }">${score}</span>
      </div>
    `;
  }).join("");

  resultContainer.innerHTML = `
  <div class="flex justify-center items-center">
    <div class="max-w-xl m-2 p-4 bg-white shadow-lg rounded-lg space-y-6">
      <h2 class="text-2xl font-bold text-center font-mono text-green-600">Similarity Result</h2>
      <p class="text-center font-mono text-gray-600">Best Match Category: <span class="font-bold font-mono text-green-500">${bestMatch}</span></p>
      <p class="text-center font-mono text-gray-600">Best Match Celebrity: <span class="font-bold font-mono text-green-500">${bestCelebrity}</span></p>

      <div>
        <h3 class="text-xl font-semibold font-mono mb-2">Men</h3>
        <div class="space-y-2">${menSection}</div>
      </div>
      
      <div>
        <h3 class="text-xl font-semibold font-mono mb-2">Women</h3>
        <div class="space-y-2">${womenSection}</div>
      </div>
    </div>
  </div>
  `;
}
