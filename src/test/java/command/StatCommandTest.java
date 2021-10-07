package command;

import com.example.habrot.habrtelegrambot.command.Command;
import com.example.habrot.habrtelegrambot.command.StatCommand;

import static com.example.habrot.habrtelegrambot.command.CommandName.STAT;
import static com.example.habrot.habrtelegrambot.command.StatCommand.STAT_MESSAGE;

public class StatCommandTest extends AbstractCommandTest {
    @Override
    String getCommandName() {
        return STAT.getCommandName();
    }

    @Override
    String getCommandMessage() {
        return String.format(STAT_MESSAGE, 0);
    }

    @Override
    Command getCommand() {
        return new StatCommand(sendBotMessageService, telegramUserService);
    }
}
