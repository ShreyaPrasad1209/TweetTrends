import { AppContainer } from "./styled";
import TwitterInput from "./InputForm";
import { GlobalStyle } from "./globalStyle";

function App() {
  return (
    <>
      <GlobalStyle />
      <AppContainer>
        <TwitterInput />
      </AppContainer>
    </>
  );
}

export default App;
