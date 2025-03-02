import axios from "axios";

const API_URL = "https://clownfish-app-lf647.ondigitalocean.app/api/v1";

interface Response {
  status: string;
  message: string;
  data: ApiResponse;
}

interface Recipe {
  title: string;
  ingredients: string;
  instructions: string;
  url: string;
}

interface ApiResponse {
  response: string;
  recipes: Recipe[];
}

const searchRecipes = async (query: string) => {
  try {
    const response = await axios.post<Response>(
      `${API_URL}/recommendation/`,
      { input_prompt: query },
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    console.log(response.data.data);
    return response.data.data;
  } catch (error) {
    if (axios.isAxiosError(error) && error.response) {
      return error.response.data;
    } else {
      return { status: "error", message: "An unknown error occurred" };
    }
  }
};

export default { searchRecipes };
