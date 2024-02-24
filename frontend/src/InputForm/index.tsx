import { useState } from "react";
import {
  Container,
  Input,
  Select,
  Logo,
  Title,
  TitleLogoWrapper,
  Button
} from "./styled";
import TwitterLogo from "../assets/images/twitter-circled.svg";

const TwitterInput = () => {
  const [username, setUsername] = useState("");
  const [selectedOption, setSelectedOption] = useState("");

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
        <option value="">Select your community</option>
        <option value="option1">Option 1</option>
        <option value="option2">Option 2</option>
        <option value="option3">Option 3</option>
      </Select>
      <Button> Submit </Button>
    </Container>
  );
};

export default TwitterInput;
