def small_llm_reviewer(state: AgentState) -> AgentState:
    """
    Perform a lightweight semantic review of the proposed SQL.
    since this psudocode was assumed (Assumption 3 in 1a) that user can access every data so this component isn't that much nescessery.
    """

    review = call_small_llm(
        user_message=state["user_message"],
        sql=state["proposed_sql"],
        response_schema=StatementQualityControl 
    )

    if not review.is_consistent:
        return # error case " the quality of the statment is past due to {review.fail_reason}" past the error with state back to agentic

    return {
        **state,
        "review_feedback": None
    } # wire with postgres_sql