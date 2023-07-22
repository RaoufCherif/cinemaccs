import { Flex, Stack } from "@chakra-ui/react";

export const PageLayout: React.FC<React.PropsWithChildren<{}>> = ({
  children,
}) => {
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
        {children}
      </Stack>
    </Flex>
  );
};
