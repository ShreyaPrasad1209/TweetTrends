import { createGlobalStyle } from "styled-components";

export const GlobalStyle = createGlobalStyle`
  html, body, #root {
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
    background-color: #ffb703;
    color: #023047;
    font-family: "Open Sans", sans-serif;
    font-optical-sizing: auto;
    font-weight: 300;
    font-style: normal;
  }
`;
