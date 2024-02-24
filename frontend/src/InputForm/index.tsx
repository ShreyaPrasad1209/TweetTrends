import { useState } from "react";
import {
  Container,
  Input,
  Select,
  Logo,
  Title,
  TitleLogoWrapper,
  Button,
  UserProfileContainer,
} from "./styled";
import TwitterLogo from "../assets/images/twitter-circled.svg";
import UserProfile from "../Users";
import { communityOptions } from "../constants";

export interface UserProfileProps {
  name: string;
  screen_name: string;
  profile_image_url_https: string;
}

const validateTwitterUsername = async (userName: string): Promise<boolean> => {
  try {
    const response = await fetch(
      `http://127.0.0.1:8000/verify_user/${userName}`
    );
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error:", error);
    return false;
  }
};

const getInfluencerNames = async (tag: string): Promise<UserProfileProps[]> => {
  try {
    const response = await fetch(`http://127.0.0.1:8000/search/?tags=${tag}`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data: UserProfileProps[] = await response.json();
    return data;
  } catch (error) {
    console.error("Error:", error);
  }
  return [];
};

const TwitterInput = () => {
  const [username, setUsername] = useState("");
  const [selectedOption, setSelectedOption] = useState("");
  const [isValidating, setIsValidating] = useState(false);
  const [isValidUsername, setIsValidUsername] = useState<boolean | null>(null);
  const [influencerNames, setInfluencerNames] = useState(
    [] as UserProfileProps[]
  );

  const handleValidation = async (username: string, tag: string) => {
    setIsValidating(true);
    const isValid = await validateTwitterUsername(username);
    setIsValidUsername(isValid);
    setIsValidating(false);
    setInfluencerNames(await getInfluencerNames(tag));
  };

  return (
    <Container>
      <TitleLogoWrapper>
        <Title>Find Twitter influencers of your community 🔎</Title>
        <Logo src={TwitterLogo} alt="Double circled Twitter Logo" />
      </TitleLogoWrapper>
      <Input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Enter your Twitter username"
      />
      <Select
        value={selectedOption}
        onChange={(e) => setSelectedOption(e.target.value)}
      >
        {communityOptions.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </Select>
      <Button
        onClick={() => {
          handleValidation(username, selectedOption);
        }}
      >
        Submit
      </Button>
      {isValidating && <p>Validating...</p>}
      {isValidUsername !== null && (
        <p>
          {isValidUsername
            ? `${username} is a valid username`
            : `${username} is an invalid username`}
        </p>
      )}

      <UserProfileContainer>
        {influencerNames.map((user) => (
          <UserProfile
            key={user.screen_name}
            name={user.name}
            screen_name={user.screen_name}
            profile_image_url_https={user.profile_image_url_https}
          />
        ))}
      </UserProfileContainer>
    </Container>
  );
};

export default TwitterInput;
