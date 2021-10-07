package command;

import com.example.habrot.habrtelegrambot.command.Command;
import com.example.habrot.habrtelegrambot.command.StopCommand;
import org.junit.jupiter.api.DisplayName;

import static com.example.habrot.habrtelegrambot.command.CommandName.STOP;
import static com.example.habrot.habrtelegrambot.command.StopCommand.STOP_MESSAGE;

@DisplayName("Unit-level testing for StopCommand")
public class StopCommandTest extends AbstractCommandTest {
    @Override
    String getCommandName() {
        return STOP.getCommandName();
    }

    @Override
    String getCommandMessage() {
        return STOP_MESSAGE;
    }

    @Override
    Command getCommand() {
        return new StopCommand(sendBotMessageService, telegramUserService);
    }
}
