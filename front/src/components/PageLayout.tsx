import { Flex, Spinner, Stack } from "@chakra-ui/react";

export const PageLayout: React.FC<
  React.PropsWithChildren<{ isLoading?: boolean }>
> = ({ isLoading, children }) => {
  return (
    <Flex
      flexDirection="column"
      width="100vw"
      backgroundColor="gray.200"
      justifyContent="center"
      alignItems="center"
    >
      <Stack
        flexDir="column"
        mb="2"
        justifyContent="center"
        alignItems="center"
      >
        {isLoading ? <Spinner /> : children}
      </Stack>
    </Flex>
  );
};
