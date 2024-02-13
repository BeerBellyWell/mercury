from app.auth import auth
from app.cancellation import cancellation
from app.saving import saving
from app.change_company import change_company
from core.config_argparse import configure_argument_parser
from core.decorators import time_check_decorator

from core.settings import driver, time_sleep_1_sec, logger


def process_cancellation_and_saving() -> None:
    logger.info('Start of cancellation process.')
    count_cancellation = 0

    while cancellation():
        count_cancellation += 1
        pass
    logger.info(f'Number of canceled invoices - {count_cancellation} pcs.')

    logger.info('Start of repayment and saving process.')
    while saving():
        pass


def process_cancellation() -> None:
    logger.info('Start of cancellation process.')
    count_cancellation = 0

    while cancellation():
        count_cancellation += 1
        pass
    logger.info(f'Number of canceled invoices - {count_cancellation} pcs.')


def process_saving() -> None:
    logger.info('Start of repayment and saving process.')
    while saving():
        pass


def full_work() -> bool:
    """Main program workflow."""
    if not auth():
        return False

    process_cancellation_and_saving()

    if not change_company():
        return False

    process_cancellation_and_saving()

    return True


def auth_and_cancellation_both() -> bool:
    """Authenticate and cancel invoices in two companies."""
    if not auth():
        return False

    process_cancellation()

    if not change_company():
        return False
    logger.info('Переход в другое предприятие выполнен.')

    process_cancellation()

    return True


def auth_and_saving_both() -> bool:
    """Authentication and storage of invoices in two company."""
    if not auth():
        return False

    process_saving()

    if not change_company():
        return False

    process_saving()

    return True


def greece_cancellation_and_saving() -> bool:
    """Canceling and saving invoices only in Greece."""
    if not auth():
        return False

    process_cancellation_and_saving()

    return True


def elizovo_opt_cancellation_and_saving() -> bool:
    """Cancellation and storage of invoices only in Elizovo wholesale."""
    if not auth():
        return False

    if not change_company():
        return False

    process_cancellation_and_saving()

    return True


def greece_cancellation_only() -> bool:
    """Authentication and cancellation of invoices in Greece."""
    if not auth():
        return False

    process_cancellation()

    return True


def elizovo_opt_cancellation_only() -> bool:
    """Authentication and cancellation of invoices in Yelizovo OPT."""
    if not auth():
        return False

    if not change_company():
        return False

    process_cancellation()

    return True


def greece_saving_only() -> bool:
    """Authentication and saving of invoices in Greece."""
    if not auth():
        return False

    process_saving()

    return True


def elizovo_opt_saving_only() -> bool:
    """Authentication and saving of invoices in elizvo wholesale."""
    if not auth():
        return False

    time_sleep_1_sec()
    if not change_company():
        return False

    process_saving()

    return True


def test() -> None:
    """func for testing."""
    import time
    logger.info('Working')
    time.sleep(2)
    logger.info('The end.')
    return True


WORKING_MODE = {
    'full-work': full_work,
    'auth-and-cancellation-both': auth_and_cancellation_both,
    'auth-and-saving-both': auth_and_saving_both,
    'greece-cancellation-and-saving': greece_cancellation_and_saving,
    'elizovo-opt-cancellation-and-saving': elizovo_opt_cancellation_and_saving,
    'greece-cancellation-only': greece_cancellation_only,
    'elizovo-opt-cancellation-only': elizovo_opt_cancellation_only,
    'greece-saving-only': greece_saving_only,
    'elizovo-opt-saving-only': elizovo_opt_saving_only,
    'test': test  # Test mode
    }


@time_check_decorator
def main():
    arg_parser = configure_argument_parser(WORKING_MODE.keys())
    args = arg_parser.parse_args()
    mode = args.mode
    try:
        logger.info(f'Starting the program in {WORKING_MODE[mode].__name__} mode.')
        results = WORKING_MODE[mode]()
        return results
    except KeyError:
        logger.error(f"Invalid mode: {mode}")
        return False
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return False


if __name__ == '__main__':
    if not main():
        logger.info('Work completed with error.')
    else:
        logger.info('Work successfully executed.')
    driver.close()
    driver.quit()
