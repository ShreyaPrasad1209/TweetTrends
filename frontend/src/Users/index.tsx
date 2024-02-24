import {
  ProfileContainer,
  ProfileImage,
  ProfileName,
  ScreenName,
  TwitterProfileLink,
  TwitterProfileDetails,
} from "./styled";

interface UserProfileProps {
  name: string;
  screen_name: string;
  profile_image_url_https: string;
}

const UserProfile = ({
  name,
  screen_name,
  profile_image_url_https,
}: UserProfileProps) => {
  const twitter_url = `https://twitter.com/${screen_name}`;
  return (
    <TwitterProfileLink href={twitter_url} target="_blank" rel="noreferrer">
      <ProfileContainer>
        <ProfileImage src={profile_image_url_https} alt={`${name}'s profile`} />
        <TwitterProfileDetails>
          <ProfileName>{name}</ProfileName>
          <ScreenName>@{screen_name}</ScreenName>
        </TwitterProfileDetails>
      </ProfileContainer>
    </TwitterProfileLink>
  );
};

export default UserProfile;
