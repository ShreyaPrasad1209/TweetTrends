import styled from "styled-components";

export const ProfileContainer = styled.div`
  display: flex;
  align-items: center;
  background-color: #f0f0f0;
  padding: 10px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.25);
  width: fit-content;
  border: 2px solid;
`;

export const ProfileImage = styled.img`
  border-radius: 50%;
  width: 50px;
  height: 50px;
  margin-right: 10px;
`;
export const ProfileName = styled.p`
  margin: 0;
  font-weight: bold;
`;

export const ScreenName = styled.p`
  margin: 0;
  color: #555;
`;

export const TwitterProfileLink = styled.a`
  color: #023047;
  text-decoration: none;
  cursor: pointer;
  &:hover,
  &:focus {
    text-decoration: underline;
    color: #196a92;
  }
`;

export const TwitterProfileDetails = styled.div``;
