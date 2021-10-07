package command;

import com.example.habrot.habrtelegrambot.command.Command;
import com.example.habrot.habrtelegrambot.command.StartCommand;
import org.junit.jupiter.api.DisplayName;

import static com.example.habrot.habrtelegrambot.command.CommandName.START;
import static com.example.habrot.habrtelegrambot.command.StartCommand.START_MESSAGE;

@DisplayName("Unit-level testing for StartCommand")
class StartCommandTest extends AbstractCommandTest {
    @Override
    String getCommandName() {
        return START.getCommandName();
    }

    @Override
    String getCommandMessage() {
        return START_MESSAGE;
    }

    @Override
    Command getCommand() {
        return new StartCommand(sendBotMessageService, telegramUserService);
    }
}
