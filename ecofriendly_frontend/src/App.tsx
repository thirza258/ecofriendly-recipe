import { useState } from "react";
import service from "./service";

interface Response {
  response: string;
  recipes: Recipe[];
}

interface Recipe {
  title: string;
  ingredients: string;
  instructions: string;
  url: string;
}

function App() {
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [query, setQuery] = useState("");
  const [cards, setCards] = useState<Recipe[]>([]); // Ensure cards is an array
  const [responseMessage, setResponseMessage] = useState(
    "What recipes do you want to see?"
  );



  const formatList = (text: string) => {
    return text
      .split(/[;.]/) 
      .map((item) => item.trim()) 
      .filter((item) => item.length > 0); 
  };

  const handleSearch = async () => {
    if (!query.trim()) {
      setError("Please enter a search query");
      return;
    }

    setError("");
    setLoading(true);

    try {
      const res: Response = await service.searchRecipes(query);

      if (res && res.recipes) {
        setResponseMessage(res.response || "Here are your recipe results:");
        setCards(res.recipes);
      } else {
        setResponseMessage("No recipes found. Try another search!");
        setCards([]);
      }
    } catch {
      setError("An error occurred while fetching recipes.");
      setCards([]); // Ensure cards is reset on error
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="relative flex flex-col items-center justify-center min-h-screen p-6 bg-gray-100">
    {/* Background Images */}
    <img
      src="/undraw_chef.svg"
      alt="Chef"
      className="absolute w-40 opacity-90  top-[10%] left-[5%] pointer-events-none"
    />
    <img
      src="/undraw_breakfast.svg"
      alt="Breakfast"
      className="absolute w-40 opacity-80  bottom-[15%] right-[10%] pointer-events-none"
    />

    <div className="w-full max-w-2xl mt-40 text-center">
      <h1 className="text-4xl font-semibold text-gray-800">
        Your Eco-Friendly Recipe Recommendations
      </h1>

      {error && <p className="mt-2 text-red-500">{error}</p>}

      <div className="mt-4 flex items-center border border-gray-300 rounded-lg shadow-sm">
        <input
          type="text"
          placeholder="Search recipes..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="w-full p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 rounded-l-lg"
          aria-label="Search recipes"
        />
        <button
          onClick={handleSearch}
          className={`p-3 text-white font-semibold rounded-r-lg transition ${
            loading
              ? "bg-blue-300 cursor-not-allowed"
              : "bg-blue-500 hover:bg-blue-600"
          }`}
          disabled={loading}
        >
          {loading ? "Searching..." : "Search"}
        </button>
      </div>
    </div>


      <p className="mt-6 text-lg text-gray-700">{responseMessage}</p>

      {loading ? (
        <p className="mt-6 text-lg text-gray-700">Loading recommendations...</p>
      ) : (
        <div className="mt-6 grid grid-cols-1 gap-6 w-full max-w-4xl mb-40">
          {cards.length > 0 ? (
            cards.map((card, index) => (
              <a
                key={index}
                href={card.url}
                target="_blank"
                rel="noopener noreferrer"
                className="p-4 bg-white shadow-lg rounded-2xl border border-gray-200 cursor-pointer hover:shadow-xl transition block"
              >
                <h3 className="text-xl font-semibold text-gray-800">
                  {card.title}
                </h3>

                <p className="mt-2 text-gray-600">
                  <strong>Ingredients:</strong>
                </p>
                <ul className="list-disc list-inside text-gray-600">
                  {formatList(card.ingredients).map((ingredient, i) => (
                    <li key={i}>{ingredient}</li>
                  ))}
                </ul>

                <p className="mt-2 text-gray-600">
                  <strong>Instructions:</strong>
                </p>
                <ol className="list-decimal list-inside text-gray-600">
                  {formatList(card.instructions).map((step, i) => (
                    <li key={i}>{step}</li>
                  ))}
                </ol>
              </a>
            ))
          ) : (
            <p className="text-gray-700 text-lg"></p>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
