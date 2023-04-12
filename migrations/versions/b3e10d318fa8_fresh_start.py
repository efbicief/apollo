"""fresh_start

Revision ID: b3e10d318fa8
Revises: 
Create Date: 2023-04-12 21:50:28.949647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b3e10d318fa8"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "counting_runs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("started_at", sa.DateTime(), nullable=False),
        sa.Column("ended_at", sa.DateTime(), nullable=False),
        sa.Column("length", sa.Integer(), nullable=False),
        sa.Column("step", sa.Numeric(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_counting_runs")),
    )
    op.create_table(
        "event_links",
        sa.Column("uid", sa.String(), nullable=False),
        sa.Column("discord_event", sa.BigInteger(), nullable=False),
        sa.Column("last_modified", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("uid", name=op.f("pk_event_links")),
        sa.UniqueConstraint("discord_event", name=op.f("uq_event_links_discord_event")),
    )
    op.create_table(
        "filament_types",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("profile", sa.String(), nullable=True),
        sa.Column("image_path", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_filament_types")),
        sa.UniqueConstraint("image_path", name=op.f("uq_filament_types_image_path")),
        sa.UniqueConstraint("name", name=op.f("uq_filament_types_name")),
    )
    op.create_table(
        "karma",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("added", sa.DateTime(), nullable=False),
        sa.Column("pluses", sa.Integer(), nullable=False),
        sa.Column("minuses", sa.Integer(), nullable=False),
        sa.Column("neutrals", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_karma")),
    )
    op.create_table(
        "rolemenu",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("msg_ref", sa.String(), nullable=False),
        sa.Column("guild_id", sa.BigInteger(), nullable=False),
        sa.Column("channel_id", sa.BigInteger(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("message_id", sa.BigInteger(), nullable=True),
        sa.Column("unique_roles", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_rolemenu")),
        sa.UniqueConstraint("msg_ref", "guild_id", name=op.f("uq_rolemenu_msg_ref")),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_uid", sa.BigInteger(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
    )
    op.create_table(
        "announcements",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("announcement_content", sa.String(), nullable=False),
        sa.Column("trigger_at", sa.DateTime(), nullable=False),
        sa.Column("triggered", sa.Boolean(), nullable=False),
        sa.Column("playback_channel_id", sa.Integer(), nullable=False),
        sa.Column("irc_name", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_announcements_user_id_users")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_announcements")),
    )
    op.create_table(
        "blacklist",
        sa.Column("topic", sa.String(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("added_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_blacklist_user_id_users")
        ),
        sa.PrimaryKeyConstraint("topic", name=op.f("pk_blacklist")),
    )
    op.create_table(
        "counting_users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("correct_replies", sa.Integer(), nullable=False),
        sa.Column("wrong_replies", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_counting_users_user_id_users")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_counting_users")),
    )
    op.create_table(
        "ignored_channels",
        sa.Column("channel", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("added_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_ignored_channels_user_id_users")
        ),
        sa.PrimaryKeyConstraint("channel", name=op.f("pk_ignored_channels")),
    )
    op.create_table(
        "karma_changes",
        sa.Column("karma_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("message_id", sa.BigInteger(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("reason", sa.String(), nullable=True),
        sa.Column("change", sa.Integer(), nullable=False),
        sa.Column("score", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["karma_id"], ["karma.id"], name=op.f("fk_karma_changes_karma_id_karma")
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_karma_changes_user_id_users")
        ),
        sa.PrimaryKeyConstraint(
            "karma_id", "user_id", "message_id", name=op.f("pk_karma_changes")
        ),
    )
    op.create_table(
        "mini_karma_channels",
        sa.Column("channel", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("added_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_mini_karma_channels_user_id_users")
        ),
        sa.PrimaryKeyConstraint("channel", name=op.f("pk_mini_karma_channels")),
    )
    op.create_table(
        "quotes",
        sa.Column("quote_id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "author_type", sa.Enum("ID", "STRING", name="mentiontype"), nullable=False
        ),
        sa.Column("quote", sa.String(), nullable=False),
        sa.Column("author_id", sa.Integer(), nullable=True),
        sa.Column("author_string", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("edited_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["author_id"], ["users.id"], name=op.f("fk_quotes_author_id_users")
        ),
        sa.PrimaryKeyConstraint("quote_id", name=op.f("pk_quotes")),
    )
    op.create_table(
        "quotes_opt_out",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "user_type", sa.Enum("ID", "STRING", name="mentiontype"), nullable=False
        ),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("user_string", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_quotes_opt_out_user_id_users")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_quotes_opt_out")),
    )
    op.create_table(
        "reminders",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("reminder_content", sa.String(), nullable=False),
        sa.Column("trigger_at", sa.DateTime(), nullable=False),
        sa.Column("triggered", sa.Boolean(), nullable=False),
        sa.Column("playback_channel_id", sa.BigInteger(), nullable=False),
        sa.Column("irc_name", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_reminders_user_id_users")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_reminders")),
    )
    op.create_table(
        "roleentry",
        sa.Column("menu_id", sa.Integer(), nullable=False),
        sa.Column("role", sa.BigInteger(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("emoji", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["menu_id"],
            ["rolemenu.id"],
            name=op.f("fk_roleentry_menu_id_rolemenu"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("menu_id", "role", name=op.f("pk_roleentry")),
    )
    op.create_table(
        "vote",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("owner_id", sa.Integer(), nullable=False),
        sa.Column(
            "type",
            sa.Enum(
                "basic", "fptp", "approval", "stv", "ranked_pairs", name="votetype"
            ),
            nullable=False,
        ),
        sa.Column("ranked_choice", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("vote_limit", sa.Integer(), nullable=False),
        sa.Column("seats", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["owner_id"], ["users.id"], name=op.f("fk_vote_owner_id_users")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_vote")),
    )
    op.create_table(
        "discord_vote",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("allowed_role_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["id"],
            ["vote.id"],
            name=op.f("fk_discord_vote_id_vote"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_discord_vote")),
    )
    op.create_table(
        "vote_choice",
        sa.Column("vote_id", sa.Integer(), nullable=False),
        sa.Column("choice_index", sa.Integer(), nullable=False),
        sa.Column("choice", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["vote_id"],
            ["vote.id"],
            name=op.f("fk_vote_choice_vote_id_vote"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("vote_id", "choice_index", name=op.f("pk_vote_choice")),
    )
    op.create_table(
        "discord_vote_message",
        sa.Column("message_id", sa.BigInteger(), nullable=False),
        sa.Column("channel_id", sa.BigInteger(), nullable=False),
        sa.Column("vote_id", sa.Integer(), nullable=False),
        sa.Column("choices_start_index", sa.Integer(), nullable=False),
        sa.Column("part", sa.Integer(), nullable=False),
        sa.Column("numb_choices", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["vote_id"],
            ["discord_vote.id"],
            name=op.f("fk_discord_vote_message_vote_id_discord_vote"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["vote_id"],
            ["vote.id"],
            name=op.f("fk_discord_vote_message_vote_id_vote"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("message_id", name=op.f("pk_discord_vote_message")),
    )
    op.create_table(
        "user_vote",
        sa.Column("vote_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("choice", sa.Integer(), nullable=False),
        sa.Column("preference", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_user_vote_user_id_users")
        ),
        sa.ForeignKeyConstraint(
            ["vote_id", "choice"],
            ["vote_choice.vote_id", "vote_choice.choice_index"],
            name=op.f("fk_user_vote_vote_id_vote_choice"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["vote_id"],
            ["vote.id"],
            name=op.f("fk_user_vote_vote_id_vote"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint(
            "vote_id", "user_id", "choice", name=op.f("pk_user_vote")
        ),
    )
    op.create_table(
        "discord_vote_choice",
        sa.Column("vote_id", sa.Integer(), nullable=False),
        sa.Column("choice_index", sa.Integer(), nullable=False),
        sa.Column("msg_id", sa.BigInteger(), nullable=False),
        sa.Column("emoji", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["msg_id"],
            ["discord_vote_message.message_id"],
            name=op.f("fk_discord_vote_choice_msg_id_discord_vote_message"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["vote_id", "choice_index"],
            ["vote_choice.vote_id", "vote_choice.choice_index"],
            name=op.f("fk_discord_vote_choice_vote_id_vote_choice"),
        ),
        sa.PrimaryKeyConstraint(
            "vote_id", "choice_index", name=op.f("pk_discord_vote_choice")
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("discord_vote_choice")
    op.drop_table("user_vote")
    op.drop_table("discord_vote_message")
    op.drop_table("vote_choice")
    op.drop_table("discord_vote")
    op.drop_table("vote")
    op.drop_table("roleentry")
    op.drop_table("reminders")
    op.drop_table("quotes_opt_out")
    op.drop_table("quotes")
    op.drop_table("mini_karma_channels")
    op.drop_table("karma_changes")
    op.drop_table("ignored_channels")
    op.drop_table("counting_users")
    op.drop_table("blacklist")
    op.drop_table("announcements")
    op.drop_table("users")
    op.drop_table("rolemenu")
    op.drop_table("karma")
    op.drop_table("filament_types")
    op.drop_table("event_links")
    op.drop_table("counting_runs")
    # ### end Alembic commands ###
